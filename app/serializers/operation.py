from typing import Literal

from pydantic import BaseModel


class Operation(BaseModel):
    op1: int
    op2: int
    operation: Literal['add', 'subtraction', 'multiplication', 'division']
