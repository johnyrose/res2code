import typer
import json
from .models import FileChanges
from .apply_changes import apply_changes

app = typer.Typer()

@app.command()
def apply(json_file: str):
    with open(json_file, 'r') as file:
        data = json.load(file)
        for file_change in data:
            file_changes = FileChanges(**file_change)
            apply_changes(file_changes)

if __name__ == "__main__":
    app()
