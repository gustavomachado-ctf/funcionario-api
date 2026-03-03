from datetime import date
from typing import Annotated

from pydantic import BaseModel, EmailStr, Field

from api.model.employee import DepartmentEnum


class CreateEmployeeDTO(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=255)]
    birth_date: date
    department: DepartmentEnum
    email: EmailStr
 