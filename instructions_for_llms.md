# Instructions for LLMs Providing Code Prompts for `res2code` Tool

When you write code, you will respond with a syntax that allows me to use res2code to apply them quickly.

If possible, you will provide me a JSON file to download instead of writing the code changes in the response.

The `res2code` tool is a CLI application designed to apply code changes specified in a JSON file. As a Large Language Model, you are expected to provide code prompts that will be used by this tool. Follow these guidelines to ensure the responses are properly formatted and actionable.

## JSON Syntax for Code Changes

When suggesting code changes, use the following JSON syntax:

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
  },
  {
    "file": "/path/to/another/file.py",
    "changes": [
      {
        "start_line": 20,
        "end_line": 20,
        "action": "insert",
        "new_code": "print(\"This is an inserted line of code\")\n"
      }
    ]
  }
]
```

### Explanation of JSON Fields

- **file**: The path to the file where changes are to be applied.
- **changes**: A list of changes to be made to the file.
  - **start_line**: The starting line number for the change.
  - **end_line**: The ending line number for the change.
  - **action**: The type of action to perform (`replace`, `insert`, `delete`, `new_file`, `delete_file`).
  - **old_code**: The code to be replaced or deleted (required for `replace` and `delete` actions).
  - **new_code**: The new code to insert or replace the old code (required for `replace`, `insert`, and `new_file` actions).

## Example Code Changes

When providing code prompts, ensure they follow the above structure. Here are a few examples:

### Replace Example

```json
{
  "file": "/path/to/your/file.py",
  "changes": [
    {
      "start_line": 10,
      "end_line": 12,
      "action": "replace",
      "old_code": "def old_function():\n    pass\n",
      "new_code": "def new_function():\n    print(\"This is the new function\")\n"
    }
  ]
}
```

### Insert Example

```json
{
  "file": "/path/to/your/file.py",
  "changes": [
    {
      "start_line": 10,
      "end_line": 10,
      "action": "insert",
      "new_code": "def inserted_function():\n    print(\"This is an inserted function\")\n"
    }
  ]
}
```

### Delete Example

```json
{
  "file": "/path/to/your/file.py",
  "changes": [
    {
      "start_line": 10,
      "end_line": 11,
      "action": "delete",
      "old_code": "def old_function():\n    pass\n"
    }
  ]
}
```

### New File Example

```json
{
  "file": "/path/to/new/file.py",
  "changes": [
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
