import asyncio
import logging
import pytz
from datetime import datetime
from concurrent import futures
from contextlib import asynccontextmanager

from sqlmodel import SQLModel, Session
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker

import grpc
import todo_pb2
import todo_pb2_grpc

from models import Task
from typing import List
# from utils import DATABASE_URL

TZ = pytz.timezone('Asia/Bangkok')

DATABASE_URL = "postgresql+asyncpg://grpc_user:grpc_password@postgres-db/grpc_db"
engine = create_async_engine(DATABASE_URL)

# async_session = sessionmaker(
#     engine, expire_on_commit=False, class_=AsyncSession
# )
# async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(
#         engine, expire_on_commit=False, class_=AsyncSession
#     )
#     async with async_session() as session:
#         yield session

def async_session_generator():
    return sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    
@asynccontextmanager
async def get_session():
    try:
        async_session = async_session_generator()
        async with async_session() as session:
            yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()

class TodoService(todo_pb2_grpc.TodoServiceServicer):

    async def CreateTask(self, request, context):
        task = Task(
            title=request.title,
            description=request.description,
            due_date=request.due_date
        )
        async with get_session() as session:
            session.add(task)
            await session.commit()
            await session.refresh(task)
        
        return todo_pb2.TaskResponse(
            id=task.id,
            title=task.title,
            description=task.description,
            due_date=task.due_date,
            done=task.done
        )

    async def ReadAllTasks(self, request, context):
        async with get_session() as session:
            result = await session.execute(select(Task).order_by(Task.id))
            tasks: List[Task] = result.scalars()
        
        return todo_pb2.TasksResponse(
            tasks=[
                todo_pb2.TaskResponse(
                    id=task.id,
                    title=task.title,
                    description=task.description,
                    due_date=task.due_date,
                    done=task.done
                ) for task in tasks
            ]
        )

    async def ReadTodayTasks(self, request, context):
        today = datetime.now(TZ).date().isoformat()
        logging.info(f"Today: {today}")
        async with get_session() as session:
            result = await session.execute(select(Task).where(Task.due_date == today).order_by(Task.id))
            tasks: List[Task] = result.scalars()
        
        return todo_pb2.TasksResponse(
            tasks=[
                todo_pb2.TaskResponse(
                    id=task.id,
                    title=task.title,
                    description=task.description,
                    due_date=task.due_date,
                    done=task.done
                ) for task in tasks
            ]
        )

    async def UpdateTask(self, request, context):
        async with get_session() as session:
            result = await session.execute(select(Task).filter(Task.id == request.id))
            task: Task = result.scalars().first()
            
            if task:
                task.title = request.title
                task.description = request.description
                task.due_date = request.due_date
                await session.commit()
                await session.refresh(task)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Task not found")
                return todo_pb2.TaskResponse()
        
        return todo_pb2.TaskResponse(
            id=task.id,
            title=task.title,
            description=task.description,
            due_date=task.due_date,
            done=task.done
        )

    async def MarkTaskDone(self, request, context):
        async with get_session() as session:
            result = await session.execute(select(Task).filter(Task.id == request.id))
            task: Task = result.scalars().first()
            
            if task:
                task.done = True
                await session.commit()
                await session.refresh(task)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Task not found")
                return todo_pb2.TaskResponse()
        
        return todo_pb2.TaskResponse(
            id=task.id,
            title=task.title,
            description=task.description,
            due_date=task.due_date,
            done=task.done
        )

    async def DeleteTask(self, request, context):
        async with get_session() as session:
            result = await session.execute(select(Task).filter(Task.id == request.id))
            task: Task = result.scalars().first()
            
            if task:
                await session.delete(task)
                await session.commit()
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Task not found")
                return todo_pb2.Empty()
        
        return todo_pb2.Empty()

async def start_server():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()
    print("Server started. Awaiting...")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start_server())
