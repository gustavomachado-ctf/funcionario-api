from datetime import date

from pydantic import BaseModel

from api.model.employee import DepartmentEnum


class ShowEmployeeDTO(BaseModel):
    id: int
    name: str
    birth_date: date
    department: DepartmentEnum
    email: str
