# Write a function that takes a list and returns a new list that contains all the elemnents of the 
# first list minus all the duplicates

def delete_duplicates(the_list):
	return list(set (the_list))

print( delete_duplicates([0,1,2,3,4,4,4,4,1,2,3,7,8,9]) )