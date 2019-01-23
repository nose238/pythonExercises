# ask the user for a number and determine whether the number is prime or not (number that has no divisors )
# use functions

def is_prime(number):
	
	for x in range(number, 0, -1):
		if x == number or x == 1:
			continue
		elif number%x == 0:
			return("It is not prime")
	return ("It is prime")

number = int(input("Give me a number and I'll tell you if it's a prime number: "))
print(is_prime(number))