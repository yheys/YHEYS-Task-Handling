import json
print("Welcome to YHEYS Task Manager.")
print(" 1.Add Task\n 2.View Tasks \n 3.Update Task \n 4.Delete Task \n 5.Exit \n  ")
#user_want=int(input("Enter your choice: "))
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(task_list):
    with open("tasks.json", "w") as file:
        json.dump(task_list, file, indent=4)

task= load_tasks( )
while True:
    user_want = int(input("Enter your choice: "))
    if user_want==1:
        add=input("Enter task description: ")
        task.append({"description":add,"complete":False})
        print("Task added!")
        save_tasks(task)

    elif user_want==2:
        if not task:
            print("No tasks found.")
        else:
            for i in task:
                if i["complete"]==True:
                    print(f' {task.index(i) +1}.{i["description"]} [ Complete ]')
                elif i["complete"]==False:
                    print(f' {task.index(i) +1}.{i["description"]} [ Not Complete ]')

    elif user_want==3:
        completed=int(input("Enter task number to mark as completed: "))
        task[completed-1]["complete"]=True
        save_tasks(task)
        print("Task updated!")

    elif user_want==4:
        which=int(input("Enter task number to delete: "))
        del task[which -1 ]
        save_tasks(task)
        print("Task deleted!")

    elif user_want==5:
        save_tasks(task)
        print("Saving tasks...\nGoodbye!")
        break
    else:
        print("Do not give invalid key!")



