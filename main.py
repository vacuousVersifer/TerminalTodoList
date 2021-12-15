from Task import Task
from List import List

def getCommand():
  choices = ["c", "r", "a", "u", "d", "e"]
  print("Do you want to (c)reate a task, (r)ead a specific task, read (a)ll tasks, (u)pdate a task, (d)elete a task, or (e)xit?")
  choice = input("(c/r/a/u/d/e): ")
  
  if choice in choices:
    return choice
  else:
    print("That is an invalid command")
    return getCommand()
    

def loop(list):
  command = getCommand()
  
  if command == "c":
    list.create()
  elif command == "r":
    list.read()
  elif command == "a":
    list.all()
  elif command == "u":
    list.update()
  elif command =="d":
    list.delete()
  else: #must be "e"
    quit()
  
  loop(list)

def start():
  print("The Vacuous Versifer's Todo List")

  list = List()
  loop(list)
  
start()
  

# Task Class (handles the data, updating, and history) 
# x = Task("Make a todo list");
# x.setItem("Make a cool todo list")
# x.getItem()
# x.getItemHistory()
# x.getData()

# List Class (handles all tasks and storage)
# x = List()
# x.create()
# x.read()
# x.all()
# x.update()
# x.delete()