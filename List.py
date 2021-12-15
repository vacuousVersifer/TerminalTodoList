from Task import Task

class List:
  def __init__(self):
    self.taskList = []

  def create(self):
    item = input("What is the task? ")
    task = Task(item)
    self.taskList.append(task)
    print("Task created")

  def read(self):
    id = input("Enter the ID of the task to read: ")

    found = False

    for task in self.taskList:
      if task.getID() == id:
        # Task things
        # Item
        # Item History
        # ID

        print("Task Summary: ")
        print("Item: " + task.getItem())
        print("Item History: " + task.getItemHistoryString())
        print("ID: " + task.getID())
        print("Date Created: " + task.getDateCreated())


        found = True
    
    if found == False:
      print("That task doens't exist")
    
  def all(self):
    print("Task List:")
    for task in self.taskList:
      print("- " + task.getItem() + " (" + task.getID() + ")")
    
  def update(self):
    id = input("Enter the ID of the task to update: ")

    found = False

    for task in self.taskList:
      if task.getID() == id:
        task.setItem(input("What should the task now be? "))
        found = True
    
    if found == False:
      print("That task doens't exist")
    
  def delete(self):
    id = input("Enter the ID of the task to delete: ")

    deleted = False

    for task in self.taskList:
      if task.getID() == id:
        self.taskList.remove(task)
        deleted = True
    
    if deleted:
      print("Task deleted")
    else:
      print("That task doesn't exist")