import os
import json
import pytest
from res2code.apply_changes import apply_changes
from res2code.models import FileChanges


@pytest.fixture
def example_file(tmp_path):
    example_file_path = tmp_path / "example.py"
    example_file_path.write_text("""def greet():
    print(\"Hello, World!\")
""")
    return example_file_path


def test_replace(example_file):
    changes = [
        {
            "file": str(example_file),
            "changes": [
                {
                    "start_line": 2,
                    "end_line": 2,
                    "action": "replace",
                    "old_code": "    print(\"Hello, World!\")\n",
                    "new_code": "    print(\"Hello, Python!\")\n"
                }
            ]
        }
    ]
    changes_json = json.dumps(changes)
    file_changes = FileChanges.parse_raw(changes_json)
    apply_changes(file_changes)

    updated_content = example_file.read_text()
    assert updated_content == """def greet():
    print(\"Hello, Python!\")
"""
