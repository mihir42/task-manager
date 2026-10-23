tasks = []

print("\nTASK MANAGER")
print("\nEnter '1' to add a task.")
print("Enter '2' to edit a task.")
print("Enter '3' to delete a task.")
print("Enter '4' to view tasks.")
print("Enter '5' to exit.")

while True:
    action = int(input("\nEnter : "))

    if action == 1 :
        task = input("Enter Task: ")
        tasks.append(task)
    elif action == 4:
        print(tasks)
    elif action == 5:
        break   