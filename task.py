from datetime import datetime

class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False
    
    def mark_completed(self):
        self.completed = True
    
    def __str__(self):
        status = "Completed"
        if not self.completed:
            status = 'Pending'
        
        return f"Task: {self.name}\nDescription: {self.description}\nDue Date: {self.due_date.strftime('%Y-%m-%d')}\nStatus: {status}"