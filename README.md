# res2code

`res2code` is a CLI tool for applying code changes specified in a JSON file.

## Installation

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py apply changes.json
```

## JSON Format

The JSON file should have the following structure:

```json
[
  {
    "file": "/path/to/your/file.py",
    "changes": [
      {
        "start_line": 10,
        "end_line": 12,
        "action": "replace",
        "old_code": "def old_function():\n    pass\n",
        "new_code": "def new_function():\n    print(\"This is the new function\")\n"
      },
      {
        "start_line": 30,
        "end_line": 30,
        "action": "delete",
        "old_code": "print(\"This line will be deleted\")\n"
      }
    ]
  }
]
```