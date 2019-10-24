import random

mysteryNumber = random.randint(1, 100)
score = 0

while True:
	guess = int(input("Pick a number between 1 and 100: "))
	score = score + 1

	if guess == mysteryNumber:
		print("Good guess")
		break
	if guess > mysteryNumber:
		print("Too High, try again")

	if guess < mysteryNumber:
		print("Too Low, try again")

print("your number of guesses is: " + str(score))