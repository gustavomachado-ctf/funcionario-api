from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from api.dto.create_employee import CreateEmployeeDTO
from api.dto.show_employee import ShowEmployeeDTO
from api.service.employee import EmployeeService

router = APIRouter(prefix="/employees")


@router.get("/")
def get_all(
    service: Annotated[EmployeeService, Depends(EmployeeService)],
    page: int = 0,
    size: int = 10,
) -> list[ShowEmployeeDTO]:
    return service.get_all(page=page, size=size)


@router.post("/")
def create(
    data: CreateEmployeeDTO,
    service: Annotated[EmployeeService, Depends(EmployeeService)],
) -> ShowEmployeeDTO:
    return service.create(data=data)


@router.get("/{id}")
def get(
    id: int,
    service: Annotated[EmployeeService, Depends(EmployeeService)],
) -> ShowEmployeeDTO:
    if not (data := service.get(id=id)):
        raise HTTPException(status_code=404, detail=f"Empregado {id} não encontrado.")

    return data

@router.put("/{id}")
def update(
    id: int,
    data: CreateEmployeeDTO,
    service: Annotated[EmployeeService, Depends(EmployeeService)],
) -> ShowEmployeeDTO:
    if not (model := service.update(id=id, data=data)):
        raise HTTPException(status_code=404, detail=f"Empregado {id} não encontrado.")

    return model

@router.delete("/{id}", status_code=204)
def delete(
    id: int,
    service: Annotated[EmployeeService, Depends(EmployeeService)],
) -> None:
    if not service.delete(id=id):
        raise HTTPException(status_code=404, detail=f"Empregado {id} não encontrado.")
