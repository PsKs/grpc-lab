import os

from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

from models import Task
from typing import List

DATABASE_URL = "postgresql+asyncpg://grpc_user:grpc_password@postgres-db/grpc_db"
# DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        yield session

class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: str

class TaskUpdate(BaseModel):
    title: str
    description: str
    due_date: str

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    due_date: str
    done: bool

class TasksOut(BaseModel):
    tasks: List[TaskOut]
