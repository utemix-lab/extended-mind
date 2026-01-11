#!/usr/bin/env python3
import json
from pathlib import Path


def migrate_node(n):
    return {
        "id": n.get("id", ""),
        "label": n.get("label", ""),
        "type": n.get("type", ""),
        "status": n.get("status", "draft"),
        "notes": n.get("notes", ""),
        "tags": n.get("tags", []),
        "importance": n.get("importance", 3),
        "refs": n.get("refs", []),
        "props": n.get("props", {}),
        "props_meta": n.get("props_meta", {}),
    }


def migrate_edge(e):
    return {
        "id": e.get("id"),
        "source": e.get("source", ""),
        "target": e.get("target", ""),
        "kind": e.get("kind") or e.get("type", ""),
        "weight": e.get("weight", 3),
        "directed": e.get("directed", True),
        "notes": e.get("notes", ""),
    }


def main() -> int:
    src = Path("cosmos/cosmos-map.v0.1.json")
    dst = Path("cosmos/cosmos-map.v0.2.json")
    if not src.exists():
        print("Missing v0.1 map")
        return 1
    data = json.loads(src.read_text(encoding="utf-8"))
    out = {
        "version": "0.2",
        "generated_at": data.get("generated_at", ""),
        "nodes": [migrate_node(n) for n in data.get("nodes", [])],
        "edges": [migrate_edge(e) for e in data.get("edges", [])],
    }
    dst.write_text(json.dumps(out, ensure_ascii=True, indent=2), encoding="utf-8")
    print(f"Wrote {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
