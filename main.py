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
print("To go back at any point Enter '0'.")

def save():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

def view():
    for j, task in enumerate(tasks, start=1):
        print(f"\n{j}. {task['Task']} ")
        print(f"Status: {task['Status']}")

def filter_view(status):
    tasks_1 = []
    for task in tasks:
        if task["Status"] == status:
            tasks_1.append(task)
    for number, task in enumerate (tasks_1, start=1):
        print()
        print(f"{number}. {task['Task']}")

def menu():
    while True:
        action = (input("\nAction: ")).lower().strip()
        while True:   
            if action == "add":
                task = input("\nEnter Task: ")
                if task == "0":
                    break
                else:
                    while True:
                        print("\nValid status names: Uninitiated, In progress & Completed")
                        status = input("\nEnter Status: ").lower().strip()
                        valid_status = ["uninitiated", "in progress", "completed"]
                        if status in valid_status:
                            tasks.append({"Task":task,"Status":status})
                            save()
                            print("\nTask added!")
                            break
                        elif status == "0":
                            break
                        else:
                            print("\nEnter valid status")

            elif action == "edit":
                if not tasks :
                    print("No tasks to edit")
                else:
                    while True:
                        try:
                            view()
                            change = int(input("\nEnter the item no. to edit: "))
                            if change == 0:
                                break
                            else:
                                change -= 1
                                if change < 0 or change >= len(tasks):
                                    print("Enter valid value")
                                else:
                                    task = input("\nEnter new task: ")
                                    while True:
                                        print("\nValid status names: Uninitiated, In progress & Completed.")
                                        print("To go back type '0'")
                                        status = input("\nEnter Status/Leave: ").lower().strip()
                                        valid_status = ["uninitiated", "in progress", "completed"]
                                        if status in valid_status:
                                            if valid_status == status:
                                                tasks[change] = {"Task":task,"Status":status}
                                                save()
                                                print("\nTask edited!\n")
                                                break
                                            elif status == "leave":
                                                break
                                        else:
                                            print("\nEnter valid status")                  
                        except ValueError:
                            print("\nedEnter valid input!")

            elif action == "delete" :
                if not tasks:
                    print("No tasks to delete")
                else:
                    view()
                    try:
                        delete = int(input("\nEnter item no. to delete: "))
                        if delete == 0:
                            break
                        delete -= 1
                        tasks.pop(delete)
                        save()
                        print("Deletion successfull!")
                    except ValueError:
                        print("\n Enter valid input")

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
                        filter_view("in progress")
                    elif choice == "3":
                        filter_view("completed")
                    elif choice == "4":
                        filter_view("uninitiated")
                    else:
                        print("Enter valid no.")
            elif action == "exit" :
                print("\nThank you for using this program.\n")
                break

            elif action == "0":
                print("\nYou are in main menu.")
                break
            else:
                print("\nInvalid action")
                break

menu()