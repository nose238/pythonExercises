# Game "cows and bulls". Randomly generate a 4 digit number. For every digit that the user guessed 
# correctly in the correct place they have a cow. For every digit that the user guessed correctly in the 
# wrong place they have a bull. Every time the user makes a guess, tell how many cows and bulls they have
# the game is over when the user guessed correctly all digits in the correct place

import random


digits = random.sample(range(10), 4)

print("\tRULES.\nI will generate 4 diferent digits. You have to write them in the correct order.")
while True:
	number_to_guess = input("Guess the 4 digit number that I generated...\
\n\nCows: the correct number in correct place. \nBulls: correct number in incorrect place.\n\n")
	cows = 0
	bulls = 0
	counter = 0

	for digit in digits:
		if int(number_to_guess[counter]) == int(digits[counter]):
			cows += 1
		counter += 1

	for pos in range(len(digits)):
		for po2 in range(len(digits)):
			if pos == po2:
				continue
			elif int(number_to_guess[po2]) == int(digits[pos]):
				bulls += 1

	if cows == 4:
		print("You're right!")
		break			

	print("Bulls =", bulls)
	print("Cows =", cows)
	print("========\n\n")
   