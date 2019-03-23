import os

# Create a new empty list named shopping_list
shopping_list = []

def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")

# Create a function named add_to_list that declares a parameter named item
  # Add the item to the list
def add_to_list(item):
  show_list()
  
  if len(shopping_list):
    position = input("Where should I add {}?\n"  
                     "Press ENTER to add to the end of the list\n"
                     "> ".format(item))
  else:
    position = 0
  
  try:
    position = abs(int(position))
  except ValueError:
    position = None
    
  if position is not None:
    shopping_list.insert(position-1, item)
  else:  
    shopping_list.append(item)
    
  show_list()
  
# Define a function named show_list that prints all the items in the list
def show_list():
  clear_screen()
  print("Here's your list:")
  
  index = 1
  
  for item in shopping_list:
    print("{}. {}".format(index, item))
    index += 1
  
  print("-"*10)
  
def remove_from_list():
  show_list()
  what_to_remove = input("What would you like to remove?\n> ")
  
  try:
    shopping_list.remove(what_to_remove)
  except ValueError:
    pass
  
  show_list()
  
def show_help():
  clear_screen()
  print("What should we pick up at the store?")
  print("""
ENTER 'DONE' to stop adding items.
ENTER 'HELP' for this help.
ENTER 'SHOW' to see your current list.
ENTER 'REMOVE' to remove an item from your list.
""")

  
show_help()
while True:
  new_item = input("> ")
  
  if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
    break
  elif new_item.upper() == "HELP":
    show_help()
    continue
  # Enable the SHOW command to show the list. Don't forget to update the help documentation.
  # Hint Make sure to run it.
  elif new_item.upper() == "SHOW":
    show_list()
    continue
  elif new_item.upper() == "REMOVE":
    remove_from_list()
  else:
    add_to_list(new_item)
  
show_list()
  