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














