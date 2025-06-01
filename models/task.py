from datetime import datetime
import uuid

class Task:
    def __init__(self, title, description):
        self.id = uuid.uuid4()
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{self.title} - {status} ({self.created_at.strftime('%y-%m-%d')})"