tasks =[]
while True:
    print("Welcome to the To-Do List App !  ")
    print("1. Add Tasks ")
    print("2. View Tasks")
    print("3. Mark Task as completed and delete task ")
    print("4. Exit")
    choice = int(input("Enter you choice : "))
    if choice == 1:
        task = input("Enter the task : ")
        tasks.append(task)
        print(f"{task} added successfully to the list")
    elif choice == 2:
        if tasks:
            print("\n Your tasks are :\n")
            for index , tasks in enumerate(tasks, start=1):
                print(f"{index}. {tasks}")
        else:
            print("No Tasks found !")
    elif choice == 3:
        if not tasks:
            print("No tasks are present to remove ")
        else:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number!")
    elif choice == 4:
        print("Exiting the To Do list app ")
        break
    else:
        print("Please enter a valid choice !")


