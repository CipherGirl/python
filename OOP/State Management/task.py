from datetime import datetime


class Task:
    """Represents a single to-do task."""
    
    def __init__(self, task_id: int, title: str):
        self.id = task_id
        self.title = title
        self.done = False
        self.created_at = datetime.now()

    def mark_done(self):
        self.done = True

    def mark_pending(self):
        self.done = False

    def __str__(self):
        status = "x" if self.done else " "
        return f"[{status}] {self.id}: {self.title}"