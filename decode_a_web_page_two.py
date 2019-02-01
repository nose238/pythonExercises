# Using requests and beautifulsuop print the full text of the article on this website:
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
import requests
from bs4 import BeautifulSoup


page = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
html_page = BeautifulSoup(page.text, features="html.parser")

paragraphs = html_page.find_all("p")

for p in paragraphs:
	if p.text == paragraphs[-7].text:
		break
	print(p.text, "\n")
	#print("paragraphs -7", paragraphs[-7])


