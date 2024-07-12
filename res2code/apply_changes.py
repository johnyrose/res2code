import os
from .models import FileChanges, Change, ActionType


def smart_lookup(file_content, old_code, new_code, start_line, end_line):
    # Returns the correct start_line and end_line for the change
    changed_lines = end_line - start_line + 1
    first_line_old_code = old_code.splitlines()[0]
    file_lines = file_content.splitlines()
    for i in range(len(file_lines)):
        if file_lines[i] == first_line_old_code:
            if "\n".join(file_lines[i:i+changed_lines]) == old_code:
                return i+1, i+changed_lines
    return start_line, end_line

def apply_replace(file_content, start_line, end_line, old_code, new_code):
    start_line, end_line = smart_lookup(file_content, old_code, new_code, start_line, end_line)
    lines = file_content.splitlines(True)
    new_lines = [f"{line}\n" for line in new_code.splitlines()]
    lines[start_line - 1:end_line] = new_lines
    return "".join(lines)

def apply_insert(file_content, start_line, new_code):
    lines = file_content.splitlines()
    new_lines = new_code.splitlines()
    lines.insert(start_line - 1, "\n".join(new_lines))
    return "\n".join(lines) + "\n"

def apply_delete(file_content, start_line, end_line, old_code):
    lines = file_content.splitlines()
    del lines[start_line - 1:end_line]
    return "\n".join(lines) + "\n"

def create_new_file(file_path, new_code):
    """Create a new file with the provided code."""
    dir_name = os.path.dirname(file_path)
    if dir_name is not "" and not os.path.exists(dir_name):
        os.makedirs(dir_name, exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(new_code)

def delete_file(file_path):
    """Delete a specified file."""
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(f"Warning: File {file_path} does not exist. Skipping delete file action.")

def apply_changes(file_changes: FileChanges):
    file_path = file_changes.file
    if not os.path.exists(file_path) and any(change.action != ActionType.new_file for change in file_changes.changes):
        print(f"Error: File {file_path} does not exist.")
        return
    
    for change in file_changes.changes:
        if change.action == ActionType.new_file:
            create_new_file(file_path, change.new_code)
        elif change.action == ActionType.delete_file:
            delete_file(file_path)
        else:
            with open(file_path, 'r') as file:
                file_content = file.read()
            
            if change.action == ActionType.replace:
                file_content = apply_replace(file_content, change.start_line, change.end_line, change.old_code, change.new_code)
            elif change.action == ActionType.insert:
                file_content = apply_insert(file_content, change.start_line, change.new_code)
            elif change.action == ActionType.delete:
                file_content = apply_delete(file_content, change.start_line, change.end_line, change.old_code)
            
            with open(file_path, 'w') as file:
                file.write(file_content)
