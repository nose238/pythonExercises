# Two player rock paper scissors game
import random

print("This is a rock-paper-scissors game. Player 1 must enter exit when the game ends")
game_running = True
game_mode = input("Choose your game mode.\n1. PLAYER VS PLAYER.\n2. PLAYER VS CPU.\n")

def who_won(p1_choice, p2_choice, gamer2):
	if p1_choice == p2_choice:
		print("It's a tie...\n")
	elif p1_choice == "1" and p2_choice == "2":
		print(gamer2, "win")
	elif p1_choice == "1" and p2_choice == "3":
		print("Player 1 win")
	elif p1_choice == "2" and p2_choice == "1":
		print("Player 1 win")
	elif p1_choice == "2" and p2_choice == "3":
		print(gamer2, "win")
	elif p1_choice == "3" and p2_choice == "1":
		print(gamer2, "win")
	elif p1_choice == "3" and p2_choice == "2":
		print("Player 1 win")

while game_running:
	current_player = "Player 1"
	print("\n\n=========================")
	print("Turn of", current_player)
	print("1. Rock.\n2. Paper.\n3. Scissors")
	p1_choice = input(current_player + ", enter the number you choose: ")
	if p1_choice == "exit":
		game_running = False
		continue
	if game_mode == "2":
		p2_choice = str(random.randrange(1,4))
		gamer2 = "CPU"
		print("Turn of", gamer2) 	
	else:
		gamer2 = "Player 2"
		print("Turn of", gamer2)
		print("1. Rock.\n2. Paper.\n3. Scissors")
		p2_choice = input(gamer2 + ", enter the number you choose: ")
	who_won(p1_choice, p2_choice, gamer2)