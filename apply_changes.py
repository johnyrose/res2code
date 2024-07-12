import os
from .models import FileChanges, Change

def apply_replace(file_content, start_line, end_line, old_code, new_code):
    lines = file_content.splitlines()
    old_lines = old_code.strip().splitlines()
    new_lines = new_code.strip().splitlines()
    if lines[start_line - 1:end_line] == old_lines:
        lines[start_line - 1:end_line] = new_lines
    else:
        print(f"Warning: Old code does not match at lines {start_line} to {end_line}. Skipping replace.")
    return "\n".join(lines) + "\n"

def apply_insert(file_content, start_line, new_code):
    lines = file_content.splitlines()
    new_lines = new_code.strip().splitlines()
    lines[start_line:start_line] = new_lines
    return "\n".join(lines) + "\n"

def apply_delete(file_content, start_line, end_line, old_code):
    lines = file_content.splitlines()
    old_lines = old_code.strip().splitlines()
    if lines[start_line - 1:end_line] == old_lines:
        del lines[start_line - 1:end_line]
    else:
        print(f"Warning: Old code does not match at lines {start_line} to {end_line}. Skipping delete.")
    return "\n".join(lines) + "\n"

def apply_changes(file_changes: FileChanges):
    file_path = file_changes.file
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return
    
    with open(file_path, 'r') as file:
        file_content = file.read()
    
    for change in file_changes.changes:
        if change.action == 'replace':
            file_content = apply_replace(file_content, change.start_line, change.end_line, change.old_code, change.new_code)
        elif change.action == 'insert':
            file_content = apply_insert(file_content, change.start_line, change.new_code)
        elif change.action == 'delete':
            file_content = apply_delete(file_content, change.start_line, change.end_line, change.old_code)
    
    with open(file_path, 'w') as file:
        file.write(file_content)
