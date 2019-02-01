# give a ordered list, then send it into a function and decide if a number (send it to the function)
# and decde if the number is in the list. USE BINARY SEARCH
import random
import math


def binary_search(the_list, number_to_search):
	if len(the_list) == 1:
		if number_to_search == the_list[0]:
			return True
		elif number_to_search != the_list[0]:
			return False
	else:
		to_search = math.ceil(len(the_list) / 2)
		print("LEN = ", str(len(the_list)))
		print("POS = ", to_search)
		if number_to_search == the_list[to_search]:
			print("si")
			return True
		elif number_to_search < the_list[to_search]:
			print("SEARCHING IN", the_list[:to_search])
			return binary_search(the_list[:to_search], number_to_search)
		elif number_to_search > the_list[to_search]:
			print("SEARCHING IN", the_list[to_search:])
			return binary_search(the_list[to_search:], number_to_search)
		


if __name__ == "__main__": 
	# a_random_list = [random.randrange(0,101) for x in range(0,50)]
	a_random_list = random.sample(range(100000), 10000)
	a_random_list.sort()

	print(a_random_list)
	number = int(input("Give me a number_to_search: "))
	print(binary_search(a_random_list, number))
