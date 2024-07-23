import utils
from fastapi import FastAPI, HTTPException

import grpc
import todo_pb2
import todo_pb2_grpc

from models import Task

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await utils.init_db()

@app.post("/tasks/", response_model=utils.TaskOut)
async def create_task(task: utils.TaskCreate):
    async with grpc.aio.insecure_channel('grpc-server:50051') as channel:
        stub = todo_pb2_grpc.TodoServiceStub(channel)
        grpc_task = todo_pb2.CreateTaskRequest(
            title=task.title,
            description=task.description,
            due_date=task.due_date
        )
        response = await stub.CreateTask(grpc_task)
    
    return utils.TaskOut(
        id=response.id,
        title=response.title,
        description=response.description,
        due_date=response.due_date,
        done=response.done
    )

@app.get("/tasks/", response_model=utils.TasksOut)
async def read_all_tasks():
    async with grpc.aio.insecure_channel('grpc-server:50051') as channel:
        stub = todo_pb2_grpc.TodoServiceStub(channel)
        response = await stub.ReadAllTasks(todo_pb2.Empty())
    
    return utils.TasksOut(tasks=[utils.TaskOut(
        id=task.id,
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        done=task.done
    ) for task in response.tasks])

@app.get("/tasks/today/", response_model=utils.TasksOut)
async def read_today_tasks():
    async with grpc.aio.insecure_channel('grpc-server:50051') as channel:
        stub = todo_pb2_grpc.TodoServiceStub(channel)
        response = await stub.ReadTodayTasks(todo_pb2.Empty())
    
    return utils.TasksOut(tasks=[utils.TaskOut(
        id=task.id,
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        done=task.done
    ) for task in response.tasks])

@app.put("/tasks/{task_id}/", response_model=utils.TaskOut)
async def update_task(task_id: int, task: utils.TaskUpdate):
    async with grpc.aio.insecure_channel('grpc-server:50051') as channel:
        stub = todo_pb2_grpc.TodoServiceStub(channel)
        grpc_task = todo_pb2.UpdateTaskRequest(
            id=task_id,
            title=task.title,
            description=task.description,
            due_date=task.due_date
        )
        response = await stub.UpdateTask(grpc_task)
    
    return utils.TaskOut(
        id=response.id,
        title=response.title,
        description=response.description,
        due_date=response.due_date,
        done=response.done
    )

@app.put("/tasks/{task_id}/done/", response_model=utils.TaskOut)
async def mark_task_done(task_id: int):
    async with grpc.aio.insecure_channel('grpc-server:50051') as channel:
        stub = todo_pb2_grpc.TodoServiceStub(channel)
        response = await stub.MarkTaskDone(todo_pb2.MarkTaskDoneRequest(id=task_id))
    
    return utils.TaskOut(
        id=response.id,
        title=response.title,
        description=response.description,
        due_date=response.due_date,
        done=response.done
    )

@app.delete("/tasks/{task_id}/")
async def delete_task(task_id: int):
    async with grpc.aio.insecure_channel('grpc-server:50051') as channel:
        stub = todo_pb2_grpc.TodoServiceStub(channel)
        await stub.DeleteTask(todo_pb2.DeleteTaskRequest(id=task_id))
    
    return {"message": "Task deleted"}
