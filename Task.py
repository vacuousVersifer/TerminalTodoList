import uuid
from datetime import datetime

class Task:
  # Commands -

  # Create a task
  def __init__(self, item):
    self.item = item
    self.id = self.makeID()
    self.dateCreated = self.makeDate()
    self.itemHistory = [(item, self.dateCreated)]

  def getItem(self):
    return self.item

  def getItemHistory(self):
    return self.itemHistory
  
  def getItemHistoryString(self):
    return " ".join(map(str, self.itemHistory))

  def getID(self):
    return self.id

  def getDateCreated(self):
    return self.dateCreated
    
  def setItem(self, newItem):
    self.item = newItem
    self.itemHistory.append((newItem, self.makeDate()))

  def getData(self):
    return (self.getItemHistory(), self.getID(), self.getDateCreated())

  def makeID(self):
    return str(uuid.uuid4())[0:8]

  def makeDate(self):
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")