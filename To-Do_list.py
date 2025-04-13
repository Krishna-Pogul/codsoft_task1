class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "✔" if task["completed"] else "✖"
                print(f"{index}. {task['task']} [{status}]")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print(f"Task {task_index} marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\nTo-Do List Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Remove Task")
            print("5. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.view_tasks()
                task_index = int(input("Enter task number to mark as completed: "))
                self.mark_completed(task_index)
            elif choice == "4":
                self.view_tasks()
                task_index = int(input("Enter task number to remove: "))
                self.remove_task(task_index)
            elif choice == "5":
                print("Exiting... Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
