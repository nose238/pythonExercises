# Use the BeautifulSoup and requests Python packages to print out a list of all article titles 
# on the new york times homepage
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.nytimes.com/")
html_page = page.text

soup = BeautifulSoup(html_page, features="html.parser")

print("\n\t\tThese are the last news in the world!\n")

titles = soup.find_all(class_="css-6h3ud0")
counter = 1
for title in titles:
	print("\t" + str(counter) + ". " +	 title.string)
	counter += 1

titles = soup.find_all("h2", "css-bzeb53")

for title in titles:
	print("\t" + str(counter) + ". " +	 title.string)
	counter += 1
