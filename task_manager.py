class TaskManager:
    def __init__(self):
        self.tasks = {}
        self._next_id = 1
    

    def add_task(self, name, description, due_date):
        task = Task(self._next_id, name, description, due_date)
        self.tasks[task.id] = task
        self._next_id += 1
        return task 

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].mark_completed()
            return True
        return False
    
    def list_tasks(self):
        return list(self.tasks.values())
    
    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
