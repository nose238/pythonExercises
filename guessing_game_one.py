# Generate a random number between 1 and 9 (including them) ask the user to guess the number and
# then tell them if they guessed too low or too high or exactly right. Keep the game until the 
# user type exit

import random

mistery_number = random.randrange(1,10)
game = True

guessed = input("I'm thinking about a number between 1 and 9 ... could you guess it?\nType exit to end the game: \n")

while game:
	if guessed == "exit":
		game = False
		continue
	elif int(guessed) == mistery_number:
		print("You're right!!!")
		print("New number generated...")
		mistery_number = random.randrange(1,10)
	elif int(guessed) < mistery_number:
		print("Too low my frind...")
	elif int(guessed) > mistery_number:
		print("Too high my frind...")
	guessed = input("Try again: ")

