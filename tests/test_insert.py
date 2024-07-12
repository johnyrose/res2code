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
def insert_changes_file(tmp_path, example_file):
    changes = [
        {
            "file": str(example_file),
            "changes": [
                {
                    "start_line": 3,
                    "end_line": 3,
                    "action": "insert",
                    "new_code": '    print("This is a new line")'
                }
            ]
        }
    ]
    changes_file_path = tmp_path / "insert_changes.json"
    changes_file_path.write_text(json.dumps(changes))
    return changes_file_path

def test_insert_cli(example_file, insert_changes_file):
    runner = CliRunner()
    result = runner.invoke(app, [str(insert_changes_file)])
    assert result.exit_code == 0

    updated_content = example_file.read_text()
    assert updated_content == """def greet():
    print("Hello, World!")
    print("This is a new line")
"""

def test_insert_subprocess(example_file, insert_changes_file):
    result = os.system(f"python main.py {str(insert_changes_file)}")
    assert result == 0

    updated_content = example_file.read_text()
    assert updated_content == """def greet():
    print("Hello, World!")
    print("This is a new line")
"""
