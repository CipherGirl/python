from enum import IntEnum
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


class TodoBase(BaseModel): # Used to define a schema
    title: str = Field(..., min_length=3, max_length=512, description="Title for the todo")
    description: str = Field(..., description="Description of the todo")
    priority: Priority  = Field(default=Priority.LOW, description="Priority of the todo")

class TodoCreate(TodoBase):
    pass

# Used for the repsonse
class Todo(TodoBase):
    todo_id: int = Field(..., description="Unique identifier for the todo") 

class TodoUpdate(BaseModel):
    title:  Optional[str] = Field(None, min_length=3, max_length=512, description="Title for the todo")
    description:  Optional[str] = Field(None, description="Description of the todo")
    priority:  Optional[Priority]  = Field(None, description="Priority of the todo")


all_todos: List[Todo] = [
    Todo(todo_id=1, title='Study', description='Complete module 4 of python learning', priority=Priority.HIGH),
    Todo(todo_id=2, title='Cook', description='Cook dinner for family', priority=Priority.MEDIUM),
    Todo(todo_id=3, title='Read', description='Read Atomic Habits', priority=Priority.LOW),
    Todo(todo_id=4, title='Journal', description='Track All the Habits', priority=Priority.LOW),
    Todo(todo_id=5, title='Activity', description='Walk 5k Steps', priority=Priority.LOW),
]


@api.get("/todos")
def get_all_todos():
    return  all_todos

@api.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@api.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1
    new_todo = Todo(
        todo_id=new_todo_id,
        title=todo.title,
        description=todo.description,
        priority=todo.priority
    )

    all_todos.append(new_todo)

    return all_todos

@api.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.title is not None:
                todo.title = updated_todo.title
            if updated_todo.description is not None:
                todo.description = updated_todo.description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@api.delete("/todos/{todo_id}", response_model=List[Todo])
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            all_todos.pop(index)
            return all_todos
    raise HTTPException(status_code=404, detail="Todo not found")