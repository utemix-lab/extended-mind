from console_utils import build_context_cocktail, serialize_bundle_json, should_call_llm


def test_bundle_empty() -> None:
    md, bundle, citations = build_context_cocktail("", [], 5)
    assert "Context Cocktail" in md
    assert bundle["docs"] == []
    assert citations == []


def test_bundle_json() -> None:
    md, bundle, _ = build_context_cocktail(
        "q",
        [
            {
                "score": 0.42,
                "rel_path": "docs/x.md",
                "title_path": "Title",
                "text": "Body",
            }
        ],
        1,
    )
    assert md
    payload = serialize_bundle_json(bundle)
    assert "\"query\"" in payload


def test_llm_skip_without_token() -> None:
    assert not should_call_llm(True, None, "model")


if __name__ == "__main__":
    test_bundle_empty()
    test_bundle_json()
    test_llm_skip_without_token()
    print("OK")
