from pyexpat.errors import messages
from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from api.dto.create_user import CreateUserDTO
from api.dto.show_user import ShowUserDTO
from api.service.user import UserService

router = APIRouter(prefix="/users")


@router.get("/")
def get_all(
    service: Annotated[UserService, Depends(UserService)],
    page: int = 0,
    size: int = 10,
) -> list[ShowUserDTO]:
    return service.get_all(page=page, size=size)


@router.post("/")
def create(
    data: CreateUserDTO,
    service: Annotated[UserService, Depends(UserService)],
) -> ShowUserDTO:
    return service.create(data=data)


@router.get("/{id}")
def get(
    id: int,
    service: Annotated[UserService, Depends(UserService)],
) -> ShowUserDTO:
    if not (data := service.get(id=id)):
        raise HTTPException(status_code=404, detail=f"Usuário {id} não encontrado.")

    return data

@router.put("/{id}")
def update(
    id: int,
    data: CreateUserDTO,
    service: Annotated[UserService, Depends(UserService)],
) -> ShowUserDTO | None:
    if not (model := service.update(id=id, data=data)):
        raise HTTPException(status_code=404, detail=f"Usuário {id} não encontrado.")

    return model

@router.delete("/{id}", status_code=204)
def delete(
    id: int,
    service: Annotated[UserService, Depends(UserService)],
) -> None:
    if not service.delete(id=id):
        raise HTTPException(status_code=404, detail=f"Usuário {id} não encontrado.")
