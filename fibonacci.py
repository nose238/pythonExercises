# write a program that asks the user how many fibonacci numbers to generate and then generates them.

def fibonacci(how_many):
	if how_many > 1: 
		last = 0
		current = 1
		print(last)
		print(current)
		for x in range(0, how_many-2):
			showed = current + last
			last = current
			current = showed
			print(showed)
	elif how_many == 1:
		print(0)


how_many = input("How many positions do you want of the fibonacci's serie?: ")
fibonacci(int(how_many))