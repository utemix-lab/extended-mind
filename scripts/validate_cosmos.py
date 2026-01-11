#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from typing import List

from jsonschema import Draft202012Validator


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate(data_path: Path, schema_path: Path) -> List[str]:
    data = load_json(data_path)
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)
    errors = []
    for err in validator.iter_errors(data):
        errors.append(f"{err.message} (at {list(err.path)})")
    return errors


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: validate_cosmos.py <data.json> <schema.json>")
        return 2
    data_path = Path(sys.argv[1])
    schema_path = Path(sys.argv[2])
    errors = validate(data_path, schema_path)
    if errors:
        print("Validation failed:")
        for e in errors:
            print(f"- {e}")
        return 1
    print("OK: cosmos map valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
