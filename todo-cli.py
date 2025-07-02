todo = []

def menu():
    print("1. Show Tasks")
    print("2. Add Tasks")
    print("3. Check Off Tasks")
    print("4. Uncheck Tasks")
    print("5. Remove Tasks")
    print("6. Exit.\n")

def show_tasks():
    if not todo:
        print("No tasks yet!\n")
    else:
        for index, task in enumerate(todo,start=1):
            if task["done"]:
                print(f"{index}) [ ✓ ] \u001b[9m{task['title']}\u001b[0m\n")
            else:
                print(f"{index}) [ ] {task['title']}\n")

def add_tasks():
    task = input("Enter a task: ")
    todo.append({"title": task, "done": False})
    print("Task Added!\n")

def check_tasks():
    try:
        index = int(input("Enter task no. to be marked as done: ")) - 1
        if 0 <= index < len(todo):
            todo[index]["done"] = True
            print("Task marked as done!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")
    
def uncheck_tasks():
    try:
        index = int(input("Enter task no. to be marked as not done: ")) - 1
        if 0 <= index < len(todo):
            todo[index]["done"] = False
            print("Task unchecked!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def remove_tasks():
    try:
        index = int(input("Enter task no. to be removed: "))-1
        todo.pop(index)
        print(f"Task {index+1} Removed!\n")
    except(IndexError, ValueError):
        print("Please enter valid task no.")

print("Welcome to To-Do List CLI, where tasks get done with ease!")
while True:
    menu()
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            show_tasks()
        case 2:
            add_tasks()
        case 3:
            check_tasks()
        case 4:
            uncheck_tasks()
        case 5:
            remove_tasks()
        case 6:
            print("Thank You for using To-Do List CLI!")
            break
        case _:
            print("Invalid choice, choose from (1-4).")