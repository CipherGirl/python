from fastapi import FastAPI

api = FastAPI()

all_todos =[
    {'todo_id': 1, 'title': 'Study', 'description': 'Complete module 4 of python learning'},
    {'todo_id': 2, 'title': 'Cook', 'description': 'Cook dinner for family'},
    {'todo_id': 3, 'title': 'Read', 'description': 'Read Atomic Habits'},
    {'todo_id': 4, 'title': 'Journal', 'description': 'Track All the Habits'},
    {'todo_id': 5, 'title': 'Activity', 'description': 'Walk 5k Steps'},
]

@api.get("/")
def index():
    return {"message": "App is running"}

@api.get("/todos")
def get_all_todos():
    return  all_todos

@api.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    return all_todos[todo_id - 1]

@api.post("/todos")
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1
    new_todo = {
        'todo_id': new_todo_id,
        'title': todo['title'],
        'description': todo['description'],
    }

    all_todos.append(new_todo)

    return all_todos

@api.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: dict):
    all_todos[todo_id - 1] = {
        'todo_id': todo_id,
        'title': updated_todo['title'],
        'description': updated_todo['description'],
    }
    return all_todos

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    del all_todos[todo_id - 1]
    return all_todos