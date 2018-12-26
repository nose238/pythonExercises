# ask the user  for a number and print out the list of all the divisors
num = int(input("Enter a number and I'm print out its divisors: "))

for x in range(num , 0, -1):
 	if num % x == 0:
 		print(x)
