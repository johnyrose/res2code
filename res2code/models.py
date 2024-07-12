from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from enum import Enum

class ActionType(str, Enum):
    replace = 'replace'
    insert = 'insert'
    delete = 'delete'
    new_file = 'new_file'
    delete_file = 'delete_file'

class Change(BaseModel):
    start_line: Optional[int] = Field(None)
    end_line: Optional[int] = Field(None)
    action: ActionType
    old_code: Optional[str] = Field(None)
    new_code: Optional[str] = Field(None)

    @field_validator('start_line', 'end_line', mode='before')
    @classmethod
    def check_lines(cls, v, info):
        if info.data.get('action') in [ActionType.replace, ActionType.delete] and v is None:
            raise ValueError(f'{info.field_name} is required for replace and delete actions')
        return v

    @field_validator('old_code', mode='before')
    @classmethod
    def check_old_code(cls, v, info):
        if info.data.get('action') in [ActionType.replace, ActionType.delete] and not v:
            raise ValueError('old_code is required for replace and delete actions')
        return v

    @field_validator('new_code', mode='before')
    @classmethod
    def check_new_code(cls, v, info):
        if info.data.get('action') in [ActionType.replace, ActionType.insert, ActionType.new_file] and not v:
            raise ValueError('new_code is required for replace, insert, and new_file actions')
        return v

class FileChanges(BaseModel):
    file: str
    changes: List[Change]
