from collections.abc import Iterable
from typing import Annotated

from fastapi.params import Depends

from api.dto.create_user import CreateUserDTO
from api.dto.show_user import ShowUserDTO
from api.repository.user import UserRepository


class UserService:
    def __init__(self, repository: Annotated[UserRepository, Depends(UserRepository)]) -> None:
        self.repository = repository

    def get_all(self, page: int = 0, size: int = 10) -> Iterable[ShowUserDTO]:
        for model in self.repository.get_all(page=page, size=size):
            yield ShowUserDTO(
                id=model.id,
                username=model.username,
                email=model.email,
                role=model.role,
            )

    def create(self, data: CreateUserDTO) -> ShowUserDTO:
        model = self.repository.create(data=data)

        return ShowUserDTO(
            id=model.id,
            username=model.username,
            email=model.email,
            role=model.role,
        )

    def get(self, id: int) -> ShowUserDTO | None:
        if not (model := self.repository.get(id=id)):
            return None

        return ShowUserDTO(
            id=model.id,
            username=model.username,
            email=model.email,
            role=model.role,
        )

    def update(self, id: int, data: CreateUserDTO) -> ShowUserDTO | None:
        if not (model := self.repository.update(id=id, data=data)):
            return None

        return ShowUserDTO(
            id=model.id,
            username=model.username,
            email=model.email,
            role=model.role,
        )

    def delete(self, id: int) -> ShowUserDTO | None:
        if not (model := self.repository.delete(id=id)):
            return None

        return ShowUserDTO(
            id=model.id,
            username=model.username,
            email=model.email,
            role=model.role,
        )
