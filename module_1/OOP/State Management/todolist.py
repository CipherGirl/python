from task import Task

class TodoList:
    """Manages a collection of Task objects."""
    task = []
    def __init__(self):
        self._tasks = []
        self._next_id = 1  # Simple auto-increment ID

    def add(self, title: str):
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = Task(self._next_id, title)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Added task: {task}")

    def remove(self, task_id: int):
        for task in self._tasks:
            if task.id == task_id:
                self._tasks.remove(task)
                print(f"Removed task {task_id}")
                return
        print(f"No task found with ID {task_id}")

    def complete(self, task_id: int):
        for task in self._tasks:
            if task.id == task_id:
                task.mark_done()
                print(f"Completed task {task_id}")
                return
        print(f"No task found with ID {task_id}")

    def list_all(self):        
        print("All tasks:")
        for task in self._tasks:
            print(task)

    def list_pending(self):
        print("Pending tasks:")
        for task in self._tasks:
            if not task.done:
                print(task)

    def list_done(self):
        print("Completed tasks:")
        for task in self._tasks:
            if task.done:
                print(task)
