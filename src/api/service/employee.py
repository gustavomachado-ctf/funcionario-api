from collections.abc import Iterable
from typing import Annotated

from fastapi import Depends

from api.dto.create_employee import CreateEmployeeDTO
from api.dto.show_employee import ShowEmployeeDTO
from api.repository.employee import EmployeeRepository


class EmployeeService:
    def __init__(self, repository: Annotated[EmployeeRepository, Depends(EmployeeRepository)]) -> None:
        self.repository = repository

    def get_all(self, page: int = 0, size: int = 10) -> Iterable[ShowEmployeeDTO]:
        for model in self.repository.get_all(page=page, size=size):
            yield ShowEmployeeDTO(
                id=model.id,
                name=model.name,
                birth_date=model.birth_date,
                department=model.department,
                email=model.email,
            )

    def create(self, data: CreateEmployeeDTO) -> ShowEmployeeDTO:
        model = self.repository.create(data=data)

        return ShowEmployeeDTO(
            id=model.id,
            name=model.name,
            birth_date=model.birth_date,
            department=model.department,
            email=model.email,
        )

    def get(self, id: int) -> ShowEmployeeDTO | None:
        if not (model := self.repository.get(id=id)):
            return None

        return ShowEmployeeDTO(
            id=model.id,
            name=model.name,
            birth_date=model.birth_date,
            department=model.department,
            email=model.email,
        )

    def update(self, id: int, data: CreateEmployeeDTO) -> ShowEmployeeDTO | None:
        if not (model := self.repository.update(id=id, data=data)):
            return None

        return ShowEmployeeDTO(
            id=model.id,
            name=model.name,
            birth_date=model.birth_date,
            department=model.department,
            email=model.email,
        )

    def delete(self, id: int) -> ShowEmployeeDTO | None:
        if not (model := self.repository.delete(id=id)):
            return None

        return ShowEmployeeDTO(
            id=model.id,
            name=model.name,
            birth_date=model.birth_date,
            department=model.department,
            email=model.email,
        )
