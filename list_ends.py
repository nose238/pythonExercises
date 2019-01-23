# write a program thah takes a numbers and makes a new list of only the first and the last elements
# Use a function

def list_ends(the_list):
	temp = []
	temp.append(the_list[0])
	temp.append(the_list[-1])
	return temp

hello = [2,3,223,2345,5,54,3,2,3]

print(list_ends(hello))