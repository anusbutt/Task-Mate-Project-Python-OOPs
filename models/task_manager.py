from models.user import User
from models.task import Task

class Task_Manager:
    def __init__(self):
        self.users = {}

    def add_user(self, name):
        if name not in self.users:
            self.users[name] = User(name)

    def create_task(self, username, title, description):
        if username in self.users:
            task = Task(title, description)
            self.users[username].assign_task(task)
            return task
        return None
    
    def get_user_task(self, username):
        return self.users[username].get_tasks() if username in self.users else []

    def get_user(self):
        return list(self.users.keys())

    