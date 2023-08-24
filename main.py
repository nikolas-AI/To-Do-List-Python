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

        headers = ["#", "Status", "Task"]
        print(tabulate(task_data, headers=headers, tablefmt="rounded_grid"))

def main():
    todo_list = ToDoList()

    while True:
        options_data = [
            ["1", "Add Task"],
            ["2", "Mark Task as Completed"],
            ["3", "Show Tasks"],
            ["4", "Exit"]
        ]

        headers = ["Option", "Description"]
        print(tabulate(options_data, headers=headers, tablefmt="rounded_grid"))

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("\nTask added!")

       


       

       


