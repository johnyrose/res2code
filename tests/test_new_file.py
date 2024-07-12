import os
import json
import pytest
from typer.testing import CliRunner
from res2code.cli import app

@pytest.fixture
def new_file_changes_file(tmp_path):
    new_file_path = tmp_path / "new_file.py"
    changes = [
        {
            "file": str(new_file_path),
            "changes": [
                {
                    "action": "new_file",
                    "new_code": 'print("This is a new file")'
                }
            ]
        }
    ]
    changes_file_path = tmp_path / "new_file_changes.json"
    changes_file_path.write_text(json.dumps(changes))
    return changes_file_path, new_file_path

def test_new_file_cli(new_file_changes_file):
    changes_file, new_file_path = new_file_changes_file
    runner = CliRunner()
    result = runner.invoke(app, [str(changes_file)])
    assert result.exit_code == 0

    assert new_file_path.exists()
    content = new_file_path.read_text()
    assert content == 'print("This is a new file")'

def test_new_file_subprocess(new_file_changes_file):
    changes_file, new_file_path = new_file_changes_file
    result = os.system(f"python main.py {str(changes_file)}")
    assert result == 0

    assert new_file_path.exists()
    content = new_file_path.read_text()
    assert content == 'print("This is a new file")'
