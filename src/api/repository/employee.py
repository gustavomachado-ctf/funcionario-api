from collections.abc import Iterable

from sqlmodel import select

from api.dependencies import DatabaseDependency
from api.dto.create_employee import CreateEmployeeDTO
from api.model.employee import EmployeeModel


class EmployeeRepository:
    def __init__(self, db: DatabaseDependency) -> None:
        self.db = db

    def get_all(self, page: int = 0, size: int = 10) -> Iterable[EmployeeModel]:
        statement = select(EmployeeModel).limit(size).offset(page * size)

        return self.db.exec(statement)

    def create(self, data: CreateEmployeeDTO) -> EmployeeModel:
        model = EmployeeModel(
            name=data.name,
            birth_date=data.birth_date,
            department=data.department,
            email=data.email,
        )

        self.db.add(model)
        self.db.commit()
        return model

    def get(self, id: int) -> EmployeeModel | None:
        statement = select(EmployeeModel).where(EmployeeModel.id == id)

        return self.db.exec(statement).first()

    def update(self, id: int, data: CreateEmployeeDTO) -> EmployeeModel | None:
        if not (model := self.get(id=id)):
            return None

        model.name = data.name
        model.birth_date = data.birth_date
        model.department = data.department
        model.email = data.email

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return model

    def delete(self, id: int) -> EmployeeModel | None:
        if not (model := self.get(id=id)):
            return None

        self.db.delete(model)
        self.db.commit()
        return model
