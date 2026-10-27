import json

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

print(len(tasks))

print("\nTASK MANAGER")
print("\nType 'Add' to add a task.")
print("Type 'Edit' to edit a task.")
print("Type 'Delete' to delete a task.")
print("Type 'View' to view tasks.")
print("Type 'Exit' to exit.")
print("Type '0' to go back at any point.")

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
        if action == "add":
            quit = 0
            while True:
                    if quit == 1:
                        break
                    task = input("\nEnter Task: ").lower().strip()
                    if task == "0":
                        print("\nGoing back...")
                        break
                    elif task == "":
                        print("\nPlease enter a task.")
                    else:
                        while True:
                            print("\nValid status names: Uninitiated, In progress & Completed")
                            status = input("\nEnter Status: ").lower().strip()
                            valid_status = ["uninitiated", "in progress", "completed"]
                            if status in valid_status:
                                tasks.append({"Task":task,"Status":status})
                                save()
                                print("\nTask added!")
                                quit += 1
                                break
                            elif status == "0":
                                print("\nGoing back...")
                                break
                            else:
                                print("\nEnter valid status")

        elif action == "edit":
                if not tasks :
                    print("\nNo tasks to edit!")
                else:
                    view()
                    quit = 0
                    while True:
                        if quit == 1:
                            break
                        try:
                            change = int(input("\nEnter the item no. to edit: "))
                            if change == 0:
                                print("\nGoing back...")
                                break
                            else:
                                change -= 1
                                if change < 0 or change >= len(tasks):
                                    print("\nEnter valid value!")
                                else:
                                    quit = 0
                                    while True:
                                        if quit == 1:
                                            break
                                        task = input("\nEnter new task: ")
                                        if task == "0":
                                            print("\nGoing back...")
                                            break
                                        elif task == "":
                                            print("\nPlease enter a task.")
                                        else:
                                            while True:
                                                print("\nValid status names: Uninitiated, In progress & Completed.")
                                                status = input("\nEnter Status: ").lower().strip()
                                                valid_status = ["uninitiated", "in progress", "completed"]
                                                if status in valid_status:
                                                    tasks[change] = {"Task":task,"Status":status}
                                                    save()
                                                    print("\nTask edited!")
                                                    quit += 1
                                                    break
                                                elif status == "0":
                                                    print("\nGoing back...")
                                                    break
                                                else:
                                                    print("\nEnter valid status")                  
                        except ValueError:
                            print("\nEnter valid input!")

        elif action == "delete" :
                if not tasks:
                    print("\nNo tasks to delete!")
                else:
                    view()
                    quit = 0
                    while True:
                        if quit == 1:
                            break
                        try:
                            delete = int(input("\nEnter item no. to delete: "))
                            if delete == 0:
                                print("\nGoing back...")
                                break
                            elif delete < 0 or delete > len(tasks):
                                print("\nEnter valid value!")
                            else:
                                while True:
                                    confirm = input("\nTo confirm type 'delete' or '0' to cancel: ").lower().strip()
                                    if confirm == "0":
                                        print("\nGoing back...")
                                        break
                                    elif confirm == "delete":
                                        delete -= 1
                                        tasks.pop(delete)
                                        save()
                                        print("\nDeletion successfull!")
                                        quit += 1
                                        break
                                    else:
                                        print("\nEnter valid value!")
                        except ValueError:
                            print("\nEnter valid input!")

        elif action == "view" :
                quit = 0
                if not tasks :
                    print("\nNo tasks yet!")
                else:
                    print("\ntype '1' to view All taskes")
                    print("type '2' to view taskes in progress")
                    print("type '3' for finished taskes")
                    print("type '4' for uninitiated tasks")
                    while True:
                        if quit == 1:
                            break
                        choice = (input("\nstatus: "))
                        if choice == "0":
                            print("\nGoing back...")
                            break
                        elif choice == "1":
                            view()
                            quit += 1
                        elif choice == "2":
                            filter_view("in progress")
                            quit += 1
                        elif choice == "3":
                            filter_view("completed")
                            quit += 1
                        elif choice == "4":
                            filter_view("uninitiated")
                            quit += 1
                        else:
                            print("\nEnter valid no.")
        elif action == "exit" :
                print("\nThank you for using this program.\n")
                break

        elif action == "0":
                print("\nYou are already in main menu.")
                
        else:
                print("\nInvalid action!")
                
menu()