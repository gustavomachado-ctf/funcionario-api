from pydantic import BaseModel

from api.model.user import RoleEnum


class ShowUserDTO(BaseModel):
    id: int
    username: str
    email: str
    role: RoleEnum
