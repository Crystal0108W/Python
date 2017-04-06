import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e: 
		return None
	try: 
		bsobj = BeautifulSoup(html.read())
		title = bsobj.body.h1
	except AttributeError as e: 
		return None
	return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
	print("Title could not be found")
else: 
	print(title)


# To find tags based on their name and attribute
# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

html1 = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj1 = BeautifulSoup(html1)
print (bsobj1)
namelist  = bsobj1.findAll("span", {"class":"green"}) # calling bsobj1.findAll(tagName, tagAttribute) in order to get a list of all the tags on the page, rather than just the first
for name in namelist:
	print(name.get_text()) # iterate through all names in the list, and prints name.get_text() in order to seperate the content from the tags

namelist1 = bsobj1.findAll("span", {"class": "green", "class": "red"})
namelist2 = bsobj1.findAll(text = "the prince")
print (len(namelist))
alltext = bsobj1.findAll(id = "text") # a keyword argument
#print (alltext)
print (type(alltext[0])) #alltext is <class 'bs4.element.ResultSet'>; alltext[0] is <class 'bs4.element.Tag'>
print(alltext.get_text())
print(alltext[0].get_text)
# .get_text() will strip all tags from the document and returns a string containing the text only. 

# Navigating Trees -- To find tags based on their location
html2 = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj2 = BeautifulSoup(html2)

for child in bsobj2.find("table", {"id": "giftList"}).children:
	print(child)

# Dealing with Siblings
for sibling in bsobj2.find("table", {"id": "giftList"}).tr.next_siblings: # or previous_siblings
	print(sibling)

# Dealing with Parents
print (bsobj2.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

# Regular Expression
images = bsobj2.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img[0-9]\.jpg")})
for image in images:
	print(image["src"])

