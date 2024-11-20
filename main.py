import pickle
import os

class ToDoApp:
    def __init__(self, filename="tasks.pkl"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as file:
                return pickle.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f"Task '{task}' added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return

        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['task']}")
        print()

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print(f"Task {task_number} marked as complete!")
        else:
            print("Invalid task number!")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task '{removed['task']}' removed!")
        else:
            print("Invalid task number!")

    def run(self):
        while True:
            print("\nTo-Do App Menu:")
            print("1. View tasks")
            print("2. Add a task")
            print("3. Mark a task as complete")
            print("4. Remove a task")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                task = input("Enter the task description: ")
                self.add_task(task)
            elif choice == "3":
                self.view_tasks()
                task_number = int(input("Enter task number to mark as complete: "))
                self.complete_task(task_number)
            elif choice == "4":
                self.view_tasks()
                task_number = int(input("Enter task number to remove: "))
                self.remove_task(task_number)
            elif choice == "5":
                print("Exiting To-Do App. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    app = ToDoApp()
    app.run()
