# Create a random list "a", then create a new list whit the even elements from "a"
import random

a = [random.randrange(10) for element in range(1, random.randrange(1,10) )]
a.sort()
print(a)
b = []
temp = [element for element in a if element%2 == 0]
for element in temp:
	if element in b:
		continue
	else:
		b.append(element)
if not b:
	print("NO EVEN ELEMENTS")
else:
	print(b)