from collections.abc import Iterable

from sqlmodel import select

from api.dependencies import DatabaseDependency
from api.dto.create_user import CreateUserDTO
from api.model.user import UserModel
from api.password import password_hash


class UserRepository:
    def __init__(self, db: DatabaseDependency) -> None:
        self.db = db

    def get_all(self, page: int = 0, size: int = 10) -> Iterable[UserModel]:
        statement = select(UserModel).limit(size).offset(page * size)

        return self.db.exec(statement).all()

    def create(self, data: CreateUserDTO) -> UserModel:
        model = UserModel(
            username=data.username,
            email=data.email,
            password_hash=password_hash(data.password),
            role=data.role,
        )

        self.db.add(model)
        self.db.commit()
        return model

    def get(self, id: int) -> UserModel | None:
        statement = select(UserModel).where(UserModel.id == id)

        return self.db.exec(statement).first()

    def update(self, id: int, data: CreateUserDTO) -> UserModel | None:
        if not (model := self.get(id=id)):
            return None

        model.username = data.username
        model.email = data.email
        model.role = data.role

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return model

    def delete(self, id: int) -> UserModel | None:
        if not (model := self.get(id=id)):
            return None

        self.db.delete(model)
        self.db.commit()
        return model
