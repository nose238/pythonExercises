# ask the user to enter their name and their age. Print out a message to tell them
# the year that they will turn 100 years old
import datetime

date = datetime.datetime.now()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("You'll be 100 until", int(date.strftime("%Y")) + 100 - age)

