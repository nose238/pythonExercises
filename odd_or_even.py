# ask the user for a number. Deppending on whether the number is odd or even print out
# an appropriate message. If the number is multiple of 4 print out a different 
# message. Then ask for 2 numbers, if "check" divides evenly into "num" print it out 


number = int(input("Enter a number: "))

if number%2 == 0: 
	print("This number is even")
else:
	print("This number is odd")

print("Furthermore, ", end="")

if number%4 == 0:
	print("it's a multiple of 4")
else:
	print("it's not a multiple of 4")

print(".....\nNow you'll enter 2 numbers...")
check = int(input("Enter the first ""number: "))
num = int(input("Enter the second number: "))

if check%num == 0:
	print(check, "divides", num, "evenly")
else:
	print(check, "divides", num, "oddly")