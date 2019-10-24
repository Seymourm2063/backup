print("Welcome to To Do List")
todoList = []
while True:
	print("Choose a to add an item")
	print("Choose r to remove an item")
	print("Choose p to print an item")
	print("Choose q to quit")
	choice = input("Make your choice: ")
	if choice == "q":
		break
	elif choice == "a":
		# add an item to the list
		myWork = input("What item would you like to add? ")
		todoList.append()
		print(todoList)
		pass # take this out when finished
	elif choice == "r":
		# remove an item from the list
		myWork = input("What item would you like to remove? ")
		todoList.remove()
		print(todoList)
		pass # take this out when finished
	elif choice == "p":
		print(todoList)
		# print the list
		pass
	else:
		print("That is not one of the choices")