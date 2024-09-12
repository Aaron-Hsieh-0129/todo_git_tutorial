tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')

def view_tasks():
    if tasks:
        print("Your tasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks to show.")

def main():
    while True:
        print("\n To-Do List Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
            # TODO: view_task
            pass
        elif choice == '3':
            # TODO: delete_task
            pass
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
