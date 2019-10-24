#conditionals

# prompt for age
age = input("What is your age: ")
age = int(age)
if age > 17:
	print("You can see an R movie")
else: # checks for 17 or less
	print("You can NOT see an R movie")

print("Have a wonderful day")

myNumber = 5
guess = int(input("Guess a number between 1 and 10"))

if guess > myNumber:
	print("Too high")
elif guess == myNumber:
	print("You got it")
else:
	print("Too low")

birthday = input("Is today your birthdays (yes or no): ")
if birthday == "yes"
	print("Happy birthday")
elif birthday == "Yes":
	print("Happy birthday")
else:
	print("Nevermind")
	
print("Thanks for playing")