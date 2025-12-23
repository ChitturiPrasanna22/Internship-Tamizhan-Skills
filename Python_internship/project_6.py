import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

# Load / Save 
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

# Add Task 
def add_task():
    title = input("Enter task title: ")
    priority = input("Enter priority (Low/Medium/High): ").capitalize()
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    
    if due_date != "":
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format")
            return

    tasks.append({
        "title": title,
        "priority": priority,
        "due_date": due_date if due_date else None,
        "done": False
    })

    save_tasks(tasks)
    print("Task added successfully!")

#  View Tasks 
def view_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Task List ---")
    for i, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["done"] else "❌ Pending"
        due = task["due_date"] if task["due_date"] else "No due date"
        print(f"{i}. {task['title']} | Priority: {task['priority']} | Due: {due} | Status: {status}")

#  Edit Task 
def edit_task():
    view_tasks()
    try:
        index = int(input("Enter task number to edit: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number")
            return
    except ValueError:
        print("Enter a valid number")
        return

    task = tasks[index]
    new_title = input(f"Enter new title (leave blank to keep '{task['title']}'): ")
    new_priority = input(f"Enter new priority (Low/Medium/High) or leave blank to keep '{task['priority']}': ").capitalize()
    new_due = input(f"Enter new due date (YYYY-MM-DD) or leave blank to keep '{task['due_date']}': ")

    if new_title:
        task['title'] = new_title
    if new_priority:
        task['priority'] = new_priority
    if new_due:
        try:
            datetime.strptime(new_due, "%Y-%m-%d")
            task['due_date'] = new_due
        except ValueError:
            print("Invalid date format, keeping previous date")

    save_tasks(tasks)
    print("Task updated successfully!")

# Delete Task
def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number")
            return
    except ValueError:
        print("Enter a valid number")
        return

    task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Task '{task['title']}' deleted successfully!")

#  Mark Task Done
def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number")
            return
    except ValueError:
        print("Enter a valid number")
        return

    tasks[index]['done'] = True
    save_tasks(tasks)
    print(f"Task '{tasks[index]['title']}' marked as done!")

#  Main Menu 
while True:
    print("\n--- To-Do List App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task as Done")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        edit_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        mark_done()
    elif choice == "6":
        print("Exiting To-Do List App")
        break
    else:
        print("Invalid choice")
