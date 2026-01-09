#!/usr/bin/env python3
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HEADING_RE = re.compile(r"^#\s+(.*)$", re.MULTILINE)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def parse_frontmatter(md: str) -> Tuple[Dict[str, Any], str]:
    m = FRONTMATTER_RE.match(md)
    if not m:
        return {}, md
    raw = m.group(1)
    body = md[m.end() :]
    data: Dict[str, Any] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if key == "tags":
            data[key] = parse_tags(val)
        else:
            data[key] = val.strip('"').strip("'")
    return data, body


def parse_tags(val: str) -> List[str]:
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if not inner:
            return []
        return [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
    if val.startswith("-"):
        return [val.lstrip("-").strip()]
    if val:
        return [val.strip()]
    return []


def extract_title(md: str, frontmatter: Dict[str, Any]) -> str:
    if frontmatter.get("title"):
        return str(frontmatter["title"])
    m = HEADING_RE.search(md)
    if m:
        return m.group(1).strip()
    return ""


def normalize_link(src_path: Path, link: str) -> Optional[str]:
    if not link or link.startswith("#"):
        return None
    if "://" in link:
        return None
    link = link.split("#", 1)[0].split("?", 1)[0]
    if not link:
        return None
    if link.startswith("/"):
        link_path = Path(link.lstrip("/"))
    else:
        link_path = (src_path.parent / link).resolve()
    try:
        rel = link_path.relative_to(Path.cwd())
    except Exception:
        return None
    if rel.suffix.lower() != ".md":
        return None
    return rel.as_posix()


def extract_links(md: str, src_path: Path) -> List[str]:
    links: List[str] = []
    for _, target in LINK_RE.findall(md):
        norm = normalize_link(src_path, target.strip())
        if norm:
            links.append(norm)
    return sorted(set(links))


def doc_id_from_path(rel_path: str) -> str:
    return rel_path.replace("/", "__").replace(".md", "")


def build_index(root: Path) -> List[Dict[str, Any]]:
    docs = []
    for path in sorted(root.rglob("*.md")):
        if path.is_absolute():
            rel_path = path.relative_to(Path.cwd()).as_posix()
        else:
            rel_path = path.as_posix()
        md = read_text(path)
        fm, body = parse_frontmatter(md)
        title = extract_title(body, fm)
        tags = fm.get("tags") if isinstance(fm.get("tags"), list) else []
        created = fm.get("created") or fm.get("date")
        updated = fm.get("updated") or fm.get("lastmod")
        doc = {
            "path": rel_path,
            "id": doc_id_from_path(rel_path),
            "title": title,
            "type": fm.get("type", ""),
            "tags": tags,
            "links": extract_links(body, path),
        }
        if created:
            doc["created"] = created
        if updated:
            doc["updated"] = updated
        docs.append(doc)
    return docs


def main() -> int:
    root = Path("docs")
    if not root.exists():
        print("docs/ not found")
        return 1
    docs = build_index(root)
    out_path = root / "_index.json"
    out_path.write_text(json.dumps(docs, ensure_ascii=True, indent=2), encoding="utf-8")
    print(f"Wrote {out_path} ({len(docs)} docs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
