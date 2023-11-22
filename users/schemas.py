from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, Field


class CreateUser(BaseModel):
    # username: str = Field(..., min_length=MinLen(3), max_length=MaxLen(20))
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr
