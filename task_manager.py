from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self._next_id = 1
    
    # Add a new task to the manager
    def add_task(self, name, description, due_date, times_done = 0):
        task = Task(self._next_id, name, description, due_date, times_done)
        self.tasks[task.id] = task
        self._next_id += 1
        return task 

    # Mark a task as completed
    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].mark_completed()
            return True
        return False

    # List all tasks in the manager     
    def list_tasks(self):
        return list(self.tasks.values())

    # Delete a task from the manager  
    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
    
    # Increment the times_done counter for a task
    def increment_task_times_done(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].increment_times_done()
            return True
        return False
