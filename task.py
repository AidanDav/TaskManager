from datetime import datetime

class Task:
    def __init__(self, task_id, name, description, due_date, times_done = 0):
        self.id = task_id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.times_done = times_done
    
    # Mark the task as completed
    def mark_completed(self):
        self.completed = True

    # Increment the times_done counter for the task
    def increment_times_done(self):
        self.times_done += 1
    
    # String representation of the task for display purposes
    def __str__(self):
        status = "Completed"
        if not self.completed:
            status = 'Pending'
        
        return f"Task: {self.name}\nDescription: {self.description}\nDue Date: {self.due_date.strftime('%Y-%m-%d')}\nStatus: {status}"