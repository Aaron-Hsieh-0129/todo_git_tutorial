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


def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.append(task_number)
        print(f'Task "{removed_task}" deleted!')
    else:
        print("Invalid task number.")

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
            pass
        elif choice == '3':
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
