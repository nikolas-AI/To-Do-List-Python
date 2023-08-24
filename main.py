from tabulate import tabulate

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True

    def show_tasks(self):
        task_data = []
        for index, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else " "
            task_data.append([index + 1, status, task['task']])

        



   

      

     

    

       


       

       


