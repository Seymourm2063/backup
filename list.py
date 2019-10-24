# make a list
carList = ["Ford", "Chevy", "Honda", "Mazda"]
print(carList)
# print individual
print(carList[1]) # prints 2nd item in list

# adds to the back of the list
carList.append("Toyota")
print(carList)

# add a variable to the list
myCar = input("What is your car make? ")
carLists.append(myCar)
print(carList)

# insert a value anywhere in the list
carList.insert(1, "Olds") # inserts in position 2, index 1
print(carList)

# remove items from a list
carList.remove("Olds") # remove a specific item
print(carList)
# carList.remove("Olds") # What happens if the item doesn't exist?
# remove by index
carList.pop(2) # removes the 3rd item
for car in carList:
	print("My favorite car is " + car)

numberList = [5, 7, 3, 12, 55, 3, 9, 10]
sum = 0
# loop through numberList and add each to the sum
for num in munberList:
	sum = sum = num

print(sum)

# len - returns the length of a list
print(lens(numberList))
print(numberList[len(numberList) - 1])

# check if a item is in a list
# if item in list

if "Toyota" in carList:
	print("So you like Toyotas")
else: 
	print("So you don't like Toyotas")