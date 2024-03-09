from scheduler import run_scheduler
from db import create_task, read_tasks, update_task, delete_task, initialize_database

def print_menu():
    print("\nTask Scheduler Menu:")
    print("1. Create Task")
    print("2. Read Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Run Scheduler")
    print("6. Exit")

def handle_choice(choice):
    if choice == "1":
        name = input("Enter task name: ")
        execution_time = input("Enter execution time (YYYY-MM-DD HH:MM:SS): ")
        create_task(name, execution_time)
        print("Task created successfully.")

    elif choice == "2":
        tasks = read_tasks()
        if tasks:
            print("Scheduled tasks:")
            for task in tasks:
                print(task)
        else:
            print("No tasks scheduled.")

    elif choice == "3":
        task_id = input("Enter task ID to update: ")
        new_name = input("Enter new task name: ")
        new_execution_time = input("Enter new execution time (YYYY-MM-DD HH:MM:SS): ")
        update_task(task_id, new_name, new_execution_time)
        print("Task updated successfully.")

    elif choice == "4":
        task_id = input("Enter task ID to delete: ")
        delete_task(task_id)
        print("Task deleted successfully.")

    elif choice == "5":
        print("Running Scheduler...")
        run_scheduler()

    elif choice == "6":
        print("Exiting Task Scheduler.")
        return False

    else:
        print("Invalid choice. Please try again.")
    return True

def main():
    print("Initializing database...")
    initialize_database()
    print("Database initialized successfully.")
    
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if not handle_choice(choice):
            break

if __name__ == "__main__":
    main()
