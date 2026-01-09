import datetime as dt
import json
from typing import Any, Dict, List, Tuple


def utc_now_iso() -> str:
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def build_context_cocktail(
    query: str, results: List[Dict[str, Any]], top_n: int
) -> Tuple[str, Dict[str, Any], List[Dict[str, Any]]]:
    n = max(0, min(top_n, len(results)))
    docs: List[Dict[str, Any]] = []
    citations: List[Dict[str, Any]] = []

    for i, r in enumerate(results[:n], 1):
        doc = {
            "rank": i,
            "score": float(r.get("score", 0.0)),
            "rel_path": r.get("rel_path", ""),
            "title_path": r.get("title_path", ""),
            "doc_kind": r.get("doc_kind"),
            "source_dir": r.get("source_dir"),
            "project": r.get("project"),
            "text": r.get("text", ""),
        }
        docs.append(doc)
        citations.append(
            {
                "score": doc["score"],
                "path": doc["rel_path"],
                "title": doc["title_path"],
                "doc_kind": doc.get("doc_kind"),
                "anchor": f"{doc['rel_path']}#chunk-{i}",
            }
        )

    bundle = {
        "query": query,
        "timestamp": utc_now_iso(),
        "docs": docs,
    }

    lines = []
    lines.append("# Context Cocktail")
    lines.append(f"Query: {query}")
    lines.append("")
    lines.append("## Constraints")
    lines.append("- Answer using only the provided sources.")
    lines.append("- If sources do not contain the answer, say you do not know.")
    lines.append("")
    lines.append("## Top fragments")
    for doc in docs:
        meta = [
            f"score={doc['score']:.4f}",
            f"path={doc['rel_path']}",
        ]
        if doc.get("doc_kind"):
            meta.append(f"doc_kind={doc['doc_kind']}")
        if doc.get("title_path"):
            meta.append(f"title={doc['title_path']}")
        lines.append(f"- [{doc['rank']}] " + ", ".join(meta))
        lines.append(doc["text"])
        lines.append("")

    bundle_md = "\n".join(lines).strip()
    return bundle_md, bundle, citations


def serialize_bundle_json(bundle: Dict[str, Any]) -> str:
    return json.dumps(bundle, ensure_ascii=False, indent=2)


def should_call_llm(llm_enabled: bool, token: str | None, model: str | None) -> bool:
    return bool(llm_enabled and token and model)
