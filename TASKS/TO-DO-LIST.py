tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to remove: "))
            removed_task = tasks.pop(task_no - 1)
            print(f"Task '{removed_task}' removed successfully!")
        except (ValueError, IndexError):
            print("Invalid task number.")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
