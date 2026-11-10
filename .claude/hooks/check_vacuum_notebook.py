"""Check the vacuum notebook's basic structure after a Claude Code edit."""

import json
import sys
from pathlib import Path


def main():
    event = json.load(sys.stdin)
    tool_input = event["tool_input"]
    edited_file = tool_input.get("notebook_path") or tool_input.get("file_path")
    if not edited_file:
        return 0

    edited_path = Path(event["cwd"], edited_file).resolve()
    project_root = Path(__file__).resolve().parents[2]
    notebook_path = project_root / "notebooks" / "vacuum_world.ipynb"
    if edited_path != notebook_path:
        return 0

    try:
        notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
        if not isinstance(notebook, dict) or notebook.get("nbformat") != 4:
            raise ValueError("expected a version 4 notebook")
        cells = notebook.get("cells")
        if not isinstance(cells, list) or not any(
            isinstance(cell, dict) and cell.get("cell_type") == "code"
            for cell in cells
        ):
            raise ValueError("expected a cell list with at least one code cell")
    except (OSError, ValueError) as error:
        print(f"Vacuum notebook structure check failed: {error}", file=sys.stderr)
        return 2

    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": "Vacuum notebook structure check passed.",
    }}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
