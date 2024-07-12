from pydantic import BaseModel
from typing import List, Optional

class Change(BaseModel):
    start_line: Optional[int] = None
    end_line: Optional[int] = None
    action: str
    old_code: Optional[str] = None
    new_code: Optional[str] = None

class FileChanges(BaseModel):
    file: str
    changes: List[Change]
