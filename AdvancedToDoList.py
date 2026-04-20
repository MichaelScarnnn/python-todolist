#-----------------------
# CLI To-Do List (Python)
#-----------------------

import json

tasks = [
    {
        "description": "Do homework",
        "completed": False,
        "priority": "high",
        "deadline": "2026-03-10"
    }
]

TASK_FILE = "advancedTasks.txt" # Task file


def load_tasks():
    """Load tasks from file into the global tasks list."""
    global tasks
    
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = [] # Dosya yoksa bos liste ile baslama
    except Exception as e:
        print(f"Error loading tasks: {e}")
        tasks = []

def save_tasks():
    """Save the current tasks list to the file."""

    try:
        with open(TASK_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)
            print("Changes are saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def list_tasks():
    if len(tasks) == 0:
        print("Task list is empty.")
        return

    print("\nYour Tasks:\n")

    for idx, task in enumerate(tasks, start=1):

        status = "✔" if task["completed"] else "✘"

        print(
            f"{idx}. [{status}] {task['description']} "
            f"(Priority: {task['priority']}, Deadline: {task['deadline']})"
        )

def add_task():
    """Add a new task with input validation."""

    description = input("Enter task description: ").strip()
    if description == "":
        print("Task cannot be empty!")
        return
    
    priority = input("Enter priority (low/medium/high): ").strip().lower()
    if priority not in ["low", "medium", "high"]:
        print("Invalid priority. Default set to 'low'.")
        priority = "low"

    deadline = input("Enter deadline (YYYY-MM-DD) or leave empty: ").strip()

    task = {
        "description": description,
        "completed": False,
        "priority": priority,
        "deadline": deadline
    }

    tasks.append(task)

    print("Task added successfully.")
    save_tasks() # Save immediately
    
def edit_task():
    """Edit an existing task by number."""
    if len(tasks) == 0:
        print("Task list is empty. Nothing to edit.\n")
        return
    list_tasks()

    try:
        num = int(input("Enter task number to edit: "))
        if num < 1 or num > len(tasks):
            print("Invalid task number!\n")
            return
        
        task = tasks[num-1]

        new_description = input("New description: ").strip()
        if new_description:
            task["description"] = new_description

        new_priority = input("New priority (low/medium/high): ").strip().lower()
        if new_priority in ["low", "medium", "high"]:
            task["priority"] = new_priority

        new_deadline = input("New deadline (YYYY-MM-DD): ").strip()
        if new_deadline:
            task["deadline"] = new_deadline

        print("Task updated successfully.\n")

        save_tasks() # Save immediately
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

def complete_task():
    if len(tasks) == 0:
        print("No tasks avaliable.")
        return
    list_tasks()

    try:
        num = int(input("Enter task number to mark as completed: "))
        if num < 1 or num > len(tasks):
            print("Invalid task number!")
            return
        
        tasks[num-1]["completed"] = True
        print("Task marked as completed.")

        save_tasks() # Save immediately

    except ValueError:
        print("Please enter a valid number.")
    
def delete_task():
    """Delete a task by number."""
    if not tasks:
        print("Task list is empty. Nothing to delete.\n")
        return
    list_tasks()

    try:
        num = int(input("Enter task number to delete: "))
        if num < 1 or num > len(tasks):
            print("Invalid task number!\n")
            return
        removed_task = tasks.pop(num-1)
        print(f"Task '{removed_task}' deleted.\n")
        save_tasks() # Save immediately
    except ValueError:
        print("Invalid input! Enter a number.\n")

def show_menu():
    """"Print the main menu"""
    print("\n--- TO DO LIST ---")
    print("1 - List Tasks")
    print("2 - Add Task")
    print("3 - Edit Task")
    print("4 - Complete Task")
    print("5 - Delete Task")
    print("6 - Exit")

def main():
    """Main loop handling user selection."""
    while True:
        show_menu()
        choice = input("Select an option(1-6): ").strip()
        if choice == "1":
            #print("Listing tasks...")
            list_tasks()
            
        elif choice == "2":
            #print("Adding task...")
            add_task()
        
        elif choice == "3":
            #print("Editing task...")
            edit_task()

        elif choice == "4":
            #pring("Completed task...")
            complete_task()

        elif choice == "5":
            #print("Deleting task...")
            delete_task()

        elif choice == "6":
            print("Exiting program... See you!")
            break

        else:
            print("Invalid selection! Choose a number from 1 to 5.\n")

# Entry Point
if __name__ == "__main__":
    load_tasks()
    main()