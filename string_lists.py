# Ask the user a string and tell if it's a palindrom
string = input("Enter a string and I will tell you if it's a palindrom: ")

print("reverse string is", string[::-1])

if string == string[::-1]:
	print("It's a palindrom")
else:
	print("It's not a palindrom")
