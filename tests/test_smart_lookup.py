import os
import json
import pytest
from typer.testing import CliRunner
from res2code.cli import app
from res2code.apply_changes import smart_lookup

@pytest.fixture
def example_file(tmp_path):
    example_file_path = tmp_path / "example.py"
    example_file_path.write_text("""
def greet():
    print("Hello, World!")
    
def farewell():
    print("Goodbye, World!")
""")
    return example_file_path

@pytest.fixture
def smart_lookup_changes_file(tmp_path, example_file):
    changes = [
        {
            "file": str(example_file),
            "changes": [
                {
                    "start_line": 2,
                    "end_line": 2,
                    "action": "replace",
                    "old_code": '    print("Hello, World!")',
                    "new_code": '    print("Hello, Python!")'
                }
            ]
        }
    ]
    changes_file_path = tmp_path / "smart_lookup_changes.json"
    changes_file_path.write_text(json.dumps(changes))
    return changes_file_path

def test_smart_lookup():
    file_content = """
def greet():
    print("Hello, World!")
    
def farewell():
    print("Goodbye, World!")
"""
    old_code = '    print("Hello, World!")'
    new_code = '    print("Hello, Python!")'
    start_line, end_line = smart_lookup(file_content, old_code, new_code, 1, 1)
    assert start_line == 3
    assert end_line == 3

def test_smart_lookup_cli(example_file, smart_lookup_changes_file):
    runner = CliRunner()
    result = runner.invoke(app, [str(smart_lookup_changes_file)])
    assert result.exit_code == 0

    updated_content = example_file.read_text()
    assert updated_content == """
def greet():
    print("Hello, Python!")
    
def farewell():
    print("Goodbye, World!")
"""

def test_smart_lookup_subprocess(example_file, smart_lookup_changes_file):
    result = os.system(f"python main.py {str(smart_lookup_changes_file)}")
    assert result == 0

    updated_content = example_file.read_text()
    assert updated_content == """
def greet():
    print("Hello, Python!")
    
def farewell():
    print("Goodbye, World!")
"""