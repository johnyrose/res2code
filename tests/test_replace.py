import os
import json
import pytest
import subprocess
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
def changes_file(tmp_path, example_file):
    changes = [
        {
            "file": str(example_file),
            "changes": [
                {
                    "start_line": 2,
                    "end_line": 2,
                    "action": "replace",
                    "old_code": '    print("Hello, World!")\n',
                    "new_code": '    print("Hello, Python!")\n'
                }
            ]
        }
    ]
    changes_file_path = tmp_path / "changes.json"
    changes_file_path.write_text(json.dumps(changes))
    return changes_file_path

def test_replace_cli(example_file, changes_file):
    runner = CliRunner()
    result = runner.invoke(app, [str(changes_file)])
    assert result.exit_code == 0

    updated_content = example_file.read_text()
    assert updated_content == """def greet():
    print("Hello, Python!")
"""

def test_replace_subprocess(example_file, changes_file):
    result = subprocess.run(["python", "main.py", str(changes_file)], capture_output=True, text=True)
    assert result.returncode == 0

    updated_content = example_file.read_text()
    assert updated_content == """def greet():
    print("Hello, Python!")
"""
