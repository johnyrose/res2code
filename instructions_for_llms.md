# Instructions for LLMs: res2code JSON Syntax

When providing code changes, YOU MUST USE the following JSON syntax in your response. This allows for quick application of changes using the res2code tool.

```json
[
  {
    "file": "relative/path/to/file.py",
    "changes": [
      {
        "action": "replace",
        "start_line": 10,
        "end_line": 12,
        "old_code": "def old_function():\n    pass\n",
        "new_code": "def new_function():\n    print(\"New function\")\n"
      },
      {
        "action": "insert",
        "start_line": 15,
        "new_code": "print(\"Inserted line\")\n"
      },
      {
        "action": "delete",
        "start_line": 20,
        "end_line": 21,
        "old_code": "print(\"Delete this\")\n"
      },
      {
        "action": "new_file",
        "new_code": "print(\"New file content\")\n"
      },
      {
        "action": "delete_file"
      }
    ]
  }
]
```

## Key Points:

1. Use relative file paths from the project root.
2. Include all necessary fields for each action type.
3. Ensure correct JSON formatting.
4. Provide accurate line numbers and code snippets.
5. Use an array of objects for multiple file changes.

Always respond with this JSON syntax when suggesting code changes.  "changes": [
    {
      "action": "new_file",
      "new_code": "def new_function():\n    print(\"This is a new file with a new function\")\n"
    }
  ]
}
```

### Delete File Example

```json
{
  "file": "/path/to/delete/file.py",
  "changes": [
    {
      "action": "delete_file"
    }
  ]
}
```

## How to Respond

When asked to provide code changes, respond with a JSON block that follows the specified structure. Ensure the code changes are clear, accurate, and correspond to the correct line numbers in the target file.

If multiple files are involved, include separate objects for each file in the JSON array.

Keep the following points in mind:
- Always specify both `start_line` and `end_line` where applicable.
- Ensure `old_code` and `new_code` match the specified action.
- Validate the syntax and structure of the JSON before responding.

By adhering to these guidelines, you can effectively use the `res2code` tool to apply code changes accurately and efficiently.
