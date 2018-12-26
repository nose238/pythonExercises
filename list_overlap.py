# Take two ranndom lists and write a program that returns a list that
# contains only the elements in common between the lists (whitout duplicate)
# randomly generate the 2 lists
import random

list1 = [random.randrange(10) for x in range(1, random.randrange(2, 10)) ]
list2 = [random.randrange(10) for x in range(1, random.randrange(2, 10)) ]
list1.sort()
list2.sort()
between = [element for element in list1 if element in list2]
output = []

for element in between:
	if element not in output:
		output.append(element)

print(list1)
print(list2)
print(between)
print(output)