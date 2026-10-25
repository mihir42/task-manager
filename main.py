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
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

def view():
    for j, task in enumerate(tasks, start=1):
        print(f"\n{j}. {task['Task']} ")
        print(f"Status: {task['Status']}")

while True:
    action = (input("\nAction : ")).lower().strip()
    if action == "add":
        task = input("\nEnter Task: ")
        print("\nvalid status names (Case sensetive): Uninitiated, In progress & Completed")
        status = input("\nEnter status: ")
        tasks.append({"Task":task,"Status":status})
        save()

    elif action == "edit":
        if not tasks :
            print("No tasks to edit")
        else:
            view()
            change = int(input("\nEnter the item no. to edit: "))
            edit_1 = input("\nEnter new task: ")
            print("\nvalid status names (Case sensetive): Uninitiated, In progress & Completed.")
            edit_2 = input("\nEnter status: ")
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
            print("\ntype '1' to view All taskes")
            print("type '2' to view taskes in progress")
            print("type '3' for finished taskes")
            print("type '4' for uninitiated tasks")
            choice = (input("\nstatus: "))
            if choice == "1":
                view()
            elif choice == "2":
                tasks_1 = []
                for task in tasks:
                    if task["Status"] == "In progress":
                        tasks_1.append(task)
                for number, task in enumerate (tasks_1, start=1):
                    print()
                    print(f"{number}. {task['Task']}")
            elif choice == "3":
                tasks_1 = []
                for task in tasks:
                    if task["Status"] == "Completed":
                        tasks_1.append(task)
                for number, task in enumerate (tasks_1, start=1):
                    print()
                    print(f"{number}. {task['Task']}")
            elif choice == "4":
                tasks_1 = []
                for task in tasks:
                    if task["Status"] == "Uninitiated":
                        tasks_1.append(task)
                for number, task in enumerate (tasks_1, start=1):
                    print()
                    print(f"{number}. {task['Task']}")
            else:
                print("Enter valid no.")
    elif action == "exit" :
        print("\nThank you for using this program.\n")
        break

    else:
        print("Invalid action") 