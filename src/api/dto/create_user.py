from typing import Annotated

from pydantic import BaseModel, EmailStr, Field

from api.model.user import RoleEnum


class CreateUserDTO(BaseModel):
    username: Annotated[str, Field(min_length=4, max_length=20)]
    email: EmailStr
    password: Annotated[str, Field(min_length=8, max_length=64)]
    role: RoleEnum
