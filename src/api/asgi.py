import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI

from api.controller.employee import router as employee_router
from api.controller.user import router as user_router
from api.repository.database import SQLModelDatabase


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[dict[str, Any] | None]:
    with SQLModelDatabase(os.environ["DATABASE_URL"]) as db:
        _app.state.db = db
        yield


app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
app.include_router(employee_router)
