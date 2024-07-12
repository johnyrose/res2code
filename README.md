# res2code

`res2code` is a CLI tool for applying code changes specified in a JSON file.

You can install `res2code` using pip:

```
pip install git+https://github.com/johnyrose/res2code.git
```

This will install `res2code` as a CLI tool on your system.2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
After installation, you can use `res2code` as a CLI tool. Apply changes from a JSON file:

```
res2code apply changes.json
```Apply changes from a JSON file:
```
python main.py apply changes.json
```

## JSON Format

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
      },
      {
        "action": "insert",
        "start_line": 15,
        "new_code": "print(\"This is a new line\")\n"
      },
      {
        "action": "new_file",
        "new_code": "print(\"This is a new file\")\n"
      },
      {
        "action": "delete_file"
      }
    ]
  }
]
```

## Supported Actions

- `replace`: Replace code between start_line and end_line
- `delete`: Delete code between start_line and end_line
- `insert`: Insert new code at start_line
- `new_file`: Create a new file with the given content
- `delete_file`: Delete the specified file
