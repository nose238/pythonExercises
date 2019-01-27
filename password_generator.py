# Write a password generator. ask the user how strog they want their password to be
import random


def generate_weak_pass(words):
	how_many_words = random.randrange(1,4)
	password = ""
	for x in range(0, how_many_words):
		password += words[random.randrange(0,6)].lower()
	if random.randrange(0,2) == 0: 
		password += words[3]*random.randrange(1,3)
	else:
		password += words[2]*random.randrange(1,2)
	return password

def generate_medium_pass(words):
	how_many_words = random.randrange(1,4)
	password = ""
	for x in range(0, how_many_words):
		word = words[random.randrange(0,6)].lower()
		password += word.capitalize() 
	if random.randrange(0,2) == 0: 
		password += words[3]*random.randrange(1,3)
	else:
		password += words[2]*random.randrange(1,2)
	return password

def generate_strong_pass(words):
	how_many_words = random.randrange(1,4)
	password = ""
	for x in range(0, how_many_words):
		word = words[random.randrange(0,6)].lower()
		password += word.capitalize() 
	if random.randrange(0,2) == 0: 
		password += words[3]*random.randrange(1,3)
		password += words[2]
	else:
		password += words[2]*random.randrange(1,2)
		password += words[3]
	password = password.replace("e", "3")
	password = password.replace("a", "@")
	password = password.replace("o", "@")
	password = password.replace("s", "$")
	password = password.replace("i", "1")
	password = password.replace("A", "4")
	password = password.replace(" ", "_")
	return password


how_strong = int(input("This is the password generator.\nChoose how strong you want your password.\
	\nweak passwords are more likly to remember.\n1.Weak. \n2.Medium. \n3.Strong.\n\n"))

print("I'm going to ask you some information about you in order to generate a password.\n\
Just answer the following questions.")

questions = [
	"First name: ",
	"Your favorite animal: ",
	"Year when you were born: ",
	"Favorite number: ",
	"Your hobbie: ",
	"One movie you like: "
]

words = []
for question in questions:
	words.append(input(question))

if how_strong == 1:
	print(generate_weak_pass(words))

elif how_strong == 2:
	print(generate_medium_pass(words))

elif how_strong == 3:
	print(generate_strong_pass(words))
else:
	print("Choose a correct option.")
