from pydantic import BaseModel, validator
from typing import List, Optional
from enum import Enum

class ActionType(str, Enum):
    replace = 'replace'
    insert = 'insert'
    delete = 'delete'
    new_file = 'new_file'
    delete_file = 'delete_file'

class Change(BaseModel):
    start_line: Optional[int] = None
    end_line: Optional[int] = None
    action: ActionType
    old_code: Optional[str] = None
    new_code: Optional[str] = None

    @validator('start_line', 'end_line')
    def check_lines(cls, v, values, **kwargs):
        if values['action'] in [ActionType.replace, ActionType.delete] and v is None:
            raise ValueError('start_line and end_line are required for replace and delete actions')
        return v

    @validator('old_code')
    def check_old_code(cls, v, values, **kwargs):
        if values['action'] in [ActionType.replace, ActionType.delete] and not v:
            raise ValueError('old_code is required for replace and delete actions')
        return v

    @validator('new_code')
    def check_new_code(cls, v, values, **kwargs):
        if values['action'] in [ActionType.replace, ActionType.insert, ActionType.new_file] and not v:
            raise ValueError('new_code is required for replace, insert, and new_file actions')
        return v

class FileChanges(BaseModel):
    file: str
    changes: List[Change]
