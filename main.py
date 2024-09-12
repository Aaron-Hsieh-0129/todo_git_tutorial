def main():
    while True:
        print("\n To-Do List Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # TODO: add_task
            pass
        elif choice == '2':
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
