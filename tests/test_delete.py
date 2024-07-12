import os
import json
import pytest
from typer.testing import CliRunner
from res2code.cli import app

@pytest.fixture
def example_file(tmp_path):
    example_file_path = tmp_path / "example.py"
    example_file_path.write_text("""def greet():
    print("Hello, World!")
""")
    return example_file_path

@pytest.fixture
def delete_changes_file(tmp_path, example_file):
    changes = [
        {
            "file": str(example_file),
            "changes": [
                {
                    "start_line": 2,
                    "end_line": 2,
                    "action": "delete",
                    "old_code": '    print("Hello, World!")'
                }
            ]
        }
    ]
    changes_file_path = tmp_path / "delete_changes.json"
    changes_file_path.write_text(json.dumps(changes))
    return changes_file_path

def test_delete_cli(example_file, delete_changes_file):
    runner = CliRunner()
    result = runner.invoke(app, [str(delete_changes_file)])
    assert result.exit_code == 0

    updated_content = example_file.read_text()
    assert updated_content == """def greet():
"""

def test_delete_subprocess(example_file, delete_changes_file):
    result = os.system(f"python main.py {str(delete_changes_file)}")
    assert result == 0

    updated_content = example_file.read_text()
    assert updated_content == """def greet():
"""
