# Madison Seymour
# Rock, Paper, Scissors
##########################################################
# Welcome Message
# 1. Print a welcome message
# 2. Prompts for a name

# Game Loop
# print score
# prompt for player choice
# get the somputer choice
# compare
# print results
# change the score variable

# Score Screen
# Print "Score: "
# Print the players score using the name
# Print the computers score
import random
# VARIABLES
pScore = 0
cScore = 0
ties = 0
computerChoices = ["rock", "paper", "scissors"]

# WELCOME MESSAGE
print("Welcome to Rock, Paper, Scissors")
playerName = input("What is your name?: ")


# Print Score
def printScore():
	print("Score: ")
	print(playerName + ":" + str(pScore))
	print("Computer Score " + str(cScore))
	print("Ties: " + str(ties))

# GAME LOOP
while True:
	printScore()
	pChoice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'q' for quit: ")
	cChoice = random.choice(computerChoices)
	if pChoice == "q":
		break
	elif pChoice == "r":
		print("You picked rock")
		if cChoice == "rock":
			print("Computer picked rock")
			print("This is a tie")
			ties = ties + 1
		elif cChoice == "paper":
			print("Computer picked paper")
			print("Paper beats rock")
			cScore = cScore + 1
		else: # scissors is the only one left
			print("Computer picked scissors")
			print("Rock beats scissors")
			pScore = pScore + 1

	elif pChoice == "p":
		print("You picked paper")
		if cChoice == "rock":
			print("Computer picked rock")
			print("Paper beats rock")
			pScore = pScore + 1
		elif cChoice == "paper":
			print("Computer picked paper")
			print("This is a tie")
			ties = ties + 1
		else:
			print("Computer picked scissors")
			print("Scissors beats paper")
			cScore = cScore + 1

	elif pChoice == "s":
		print("You picked scissors")
		if cChoice == "rock":
			print("Computer picked rock")
			print("Rock beats scissors")
			cScore = cScore + 1
		elif cChoice == "paper":
			print("Computer picked paper")
			print("Scissors beats paper")
			pScore = pScore + 1
		else:
			print("Computer picked scissors")
			print("This is a tie")
			ties = ties + 1

	else:
		print("The character you picked is not on the list")