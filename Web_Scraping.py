from bs4 import BeautifulSoup
import urllib.request
r = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_highest-grossing_films_in_China").read()
soup = BeautifulSoup(r, "lxml")
#print (soup.title)
#print (soup.title.string)
all_links = soup.findAll("a")
print (type(all_links))
for link in all_links:
    link.get("href")

all_tables=soup.findAll("table")
print (all_tables)
right_table = soup.find("table", class_="wikitable sortable")
print (right_table)

A=[]
B=[]
C=[]
D=[]
E=[]


for row in right_table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 6:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))

import pandas as pd
df = pd.DataFrame(A, columns = ["Rank"])
df["Title"]=B
df["Gross"]=C
df["Country"]=D
df["Year"]=E
df
