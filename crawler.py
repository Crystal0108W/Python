from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

# Traversing a Single Domain
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
# Seperate the links link to articles from other links
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$")):
	if 'href' in link.attrs:
		print (link.attrs['href'])


# Create a function 
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org" + articleUrl)
	bsObjA = BeautifulSoup(html)
	return bsObjA.find("div", {"id": "bodyContent"}).findAll("a",
		href = re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links)> 0:
	newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
	print(newArticle)
	links = getLinks(newArticle) 

#######################################################################
pages = set()
def getLinks (pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org" + pageUrl)
	bsObj = BeautifulSoup(html)
	for link in bsObj.findAll("a", href = re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages: 
				newPage = link.attrs['href']
				print (newPage)
				pages.add(newPage)
				getLinks(newPage)

	getLinks("")

#######################################################################
# Crawler + Data Gathering

pages = set()
def getLinks(pageUrl):
	global pages 
	html = urlopen("http://en.wikipedia.org" + pageUrl)
	bsObj = BeautifulSoup(html)
	try: 
		print (bsObj.h1.get_text())
		print (bsObj.find(id = "mw-content-text").findAll("p")[0])
		print (bsObj.find(id = "ca-edit").find("span").find("a").attrs['href'])
	except AttributeError: 
		print ("This page is missing something! No worries though!")

	for link in bsObj.findAll("a", href = re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
		cs		newPage = link.attrs['href']
				print ("---------------\n"+newPage)
				pages.add(newPage)
				getLinks(newPage)

getLinks("/wiki/Kevin_Bacon")



