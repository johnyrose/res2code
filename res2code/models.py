from pydantic import BaseModel, Field
from typing import List, Optional

class Change(BaseModel):
    start_line: int
    end_line: int
    action: str
    old_code: Optional[str] = None
    new_code: Optional[str] = None

class FileChanges(BaseModel):
    file: str
    changes: List[Change]
