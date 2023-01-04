todos = []

while True:
    user_action = input("Type add, show or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case "show":
            for item in todos:
                print('-' + item)
        case "exit":
            break

print ("Bye!")

tasks = []

def add_task(task):
  tasks.append(task)
  print("Task added:", task)

def complete_task(task):
  tasks.remove(task)
  print("Task completed:", task)

def list_tasks():
  print("Current tasks:")
  for task in tasks:
    print(task)

while True:
  action = input("What would you like to do? (add/complete/list) ")
  if action == "add":
    task = input("Enter a task: ")
    add_task(task)
  elif action == "complete":
    task = input("Enter a task to complete: ")
    complete_task(task)
  elif action == "list":
    list_tasks()
  else:
    print("Invalid input.")















