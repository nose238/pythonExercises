# Write a program (using functions) that asks the user for a long string containing multiple words. Print it back
# whit the words in backwards order
def backwards_sentence(sentence):
	temp = sentence.split(" ")
	new_list = ""
	for element in range(len(temp)-1, -1, -1):
		new_list += temp[element] + " "
	return new_list






sentence = input("Write a sentence and I'm gonna print it out but in backwards order ... \n")
print(str(backwards_sentence(sentence)))