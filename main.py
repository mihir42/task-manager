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
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


while True:
    action = (input("\nAction : ")).lower().strip()
    if action == "add":
        task = input("Enter Task: ")
        tasks.append(task)
        save()
    elif action == "edit":
        while True:
            if tasks == []:
                print("No tasks to edit")
                break
            view()
            change = input("Enter the item to edit: ")
            if change in tasks:
                index = tasks.index(change)
                tasks[index] = input("Enter new task: ")
                print("Edit successfull!")
                save()
                break
            else:
                print("Enter valid task.")
    elif action == "delete" :
        while True:
            if not tasks:
                print("No tasks to delete")
                break
            view()
            task_1 = input("Enter the task to delete: ")
            if task_1 in tasks:
                tasks.remove(task_1)
                print("Task removed successfully!")
                save()
                break
            else:
                print("Enter valid item or check spelling.")

    elif action == "view" :
        if not tasks :
            print("No tasks yet.")
        else:
            view()
        
    elif action == "exit" :
        break
    else:
        print("Invalid action") 