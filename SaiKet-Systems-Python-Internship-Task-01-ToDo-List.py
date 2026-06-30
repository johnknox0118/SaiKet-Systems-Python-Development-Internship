"""
SaiKet Systems - Python Development Internship
Task 1: To-Do List Application

Description:
A command-line to-do list app where users can add tasks, mark them as
completed, view tasks, and delete tasks. Each task is represented using
a dictionary with 'description' and 'completed' attributes.

Skills demonstrated: Basic Python Programming, Data Structures (Dictionaries),
Conditional Statements
"""


class ToDoList:
    def __init__(self):
        # Each task is a dictionary: {"description": str, "completed": bool}
        self.tasks = []

    def add_task(self, description):
        task = {"description": description, "completed": False}
        self.tasks.append(task)
        print(f'Task added: "{description}"')

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f'Task marked as completed: "{self.tasks[index]["description"]}"')
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f'Task removed: "{removed["description"]}"')
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("\nYour to-do list is empty.\n")
            return
        print("\n----- YOUR TO-DO LIST -----")
        for i, task in enumerate(self.tasks):
            status = "✔ Done" if task["completed"] else "✘ Pending"
            print(f'{i + 1}. {task["description"]}  [{status}]')
        print("----------------------------\n")


def show_menu():
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. Exit")


def main():
    todo = ToDoList()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            description = input("Enter task description: ").strip()
            if description:
                todo.add_task(description)
            else:
                print("Task description cannot be empty.")

        elif choice == "2":
            todo.view_tasks()
            if todo.tasks:
                try:
                    index = int(input("Enter task number to mark completed: ")) - 1
                    todo.mark_completed(index)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "3":
            todo.view_tasks()
            if todo.tasks:
                try:
                    index = int(input("Enter task number to delete: ")) - 1
                    todo.delete_task(index)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            todo.view_tasks()

        elif choice == "5":
            print("Goodbye! Stay productive.")
            break

        else:
            print("Invalid choice. Please select between 1-5.")


if __name__ == "__main__":
    main()
