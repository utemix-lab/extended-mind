#!/usr/bin/env python3
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple


def load_index(path: Path) -> List[Dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def node_id(doc_id: str) -> str:
    return doc_id.replace("-", "_")


def label_for(doc: Dict) -> str:
    title = doc.get("title") or doc.get("path")
    return title.replace('"', "'")


def build_edges(docs: List[Dict]) -> Set[Tuple[str, str, str]]:
    edges: Set[Tuple[str, str, str]] = set()
    for d in docs:
        src = node_id(d["id"])
        for link in d.get("links", []):
            target = next((x for x in docs if x["path"] == link), None)
            if not target:
                continue
            dst = node_id(target["id"])
            edges.add((src, dst, "link"))
        dtype = d.get("type")
        if dtype:
            type_node = node_id(f"type__{dtype}")
            edges.add((src, type_node, "belongs-to"))
    return edges


def main() -> int:
    index_path = Path("docs/_index.json")
    if not index_path.exists():
        print("docs/_index.json not found")
        return 1
    docs = load_index(index_path)
    lines = ["graph TD"]

    for d in docs:
        nid = node_id(d["id"])
        lines.append(f'  {nid}["{label_for(d)}"]')

    types = sorted({d.get("type") for d in docs if d.get("type")})
    for t in types:
        tid = node_id(f"type__{t}")
        lines.append(f'  {tid}(["{t}"])')

    for src, dst, kind in sorted(build_edges(docs)):
        if kind == "belongs-to":
            lines.append(f"  {src} -.-> {dst}")
        else:
            lines.append(f"  {src} --> {dst}")

    out_dir = Path("docs/maps")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "graph.mmd"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
