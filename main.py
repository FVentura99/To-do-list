import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=2)

def show_menu():
    print("\n1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            for i, task in enumerate(tasks):
                status = "✔" if task["done"] else "✘"
                tasklabel = "[Optional]" if task["type"] == "optional" else "[Mandatory Task]"
                print(f"{i+1}. [{status}] {tasklabel} {task['title']}")
        elif choice == "2":
            title = input("Enter task title: ")
            optional  = input("Is the task added optional? (y/n) ").strip().lower()
            tasktype = "optional" if optional == "y" else "mandatory"
            tasks.append({"title": title, "done": False, "type": tasktype})
        elif choice == "3":
            num = int(input("Task number to complete: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]["done"] = True
        elif choice == "4":
            num = int(input("Task number to delete: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye! Have an amazing day!")
            break
        else:
            print("I am sorry, please select the imput shown on menu.")

if __name__ == "__main__":
    main()
