# create a list and pritn out all the elements that are less than 5
# then save that information into a new list 
# at the end make all again but in just one line
# ask the user for a number and return a list with numbers in the fist list that are smaller than the one given by user
numbers_list = [1, 2, 4 ,7, 8, 9, 23, 66, 12, 89, 23, 67, 298, 11, 2, 0]
new_list = []

for number in numbers_list:
	if number < 5:
		print(number)
		new_list.append(number)
	else:
		continue

print("The new list is: ", new_list)

one_line = [number for number in numbers_list if number < 5]
print("The same list written by one line is: ", one_line)