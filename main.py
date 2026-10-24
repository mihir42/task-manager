import json

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

print("\nTASK MANAGER")
print("\nType 'Add' to add a task.")
print("Type 'Edit' to edit a task.")
print("Type 'Delete' to delete a task.")
print("Type 'View' to view tasks.")
print("Type 'Exit' to exit.")

def save():
    with open("tasks.json", "w")as file:
        json.dump(tasks, file, indent=2)

def view():
    for j, task in enumerate(tasks, start=1):
        print(f"\n{j}. {task['Task']} ")
        print(f"Status: {task['Status']}")

while True:
    action = (input("\nAction : ")).lower().strip()
    if action == "add":
        task = input("Enter Task: ")
        status = input("Enter status: ")
        tasks.append({"Task":task,"Status":status})
        save()

    elif action == "edit":
        if not tasks :
            print("No tasks to edit")
        else:
            view()
            change = int(input("\nEnter the item no. to edit: "))
            edit_1 = input("Enter new task: ")
            edit_2 = input("Enter status: ")
            edit = {"Task":edit_1, "Status": edit_2}
            change -= 1
            tasks[change] = edit
            print("Edit successfull!")
            save()

    elif action == "delete" :
        if not tasks:
            print("No tasks to delete")
        else:
            view()
            delete = int(input("\nEnter item no. to delete: "))
            delete -= 1
            tasks.pop(delete)
            save()
            print("Deletion successfull!")

    elif action == "view" :
        if not tasks :
            print("No tasks yet")
        else:
            view()
        
    elif action == "exit" :
        break

    else:
        print("Invalid action") 