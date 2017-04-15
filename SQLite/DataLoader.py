import random
import string
import sqlite3

# Build connection with db
conn = sqlite3.connect('D:\sqlite\db\\my_db')
c = conn.cursor()

stats = []
# generate data
def generator():
	''' GENERATE DATA '''
	index = 0
	while len(stats) < 5000000:
		# random 8 digits string
		str = ''.join([random.choice(string.ascii_lowercase) for i in range(8)])
		t = (index, random.randint(1, 5000000), random.randint(1, 5000000), str)
		stats.append(t)
		index +=1

generator()
#print(stats)
print(len(stats))

# Create Tables
c.execute('''CREATE TABLE IF NOT EXISTS A(
				pk NUMBER PRIMARY KEY,
				ht NUMBER,
				tt NUMBER,
				ot NUMBER,
				filler CHAR(247), 
			 )''')

c.execute('''CREATE TABLE IF NOT EXISTS B(
				pk NUMBER PRIMARY KEY,
				ht NUMBER,
				tt NUMBER,
				ot NUMBER,
				filler CHAR(247), 
			 )''')

c.execute('''CREATE TABLE IF NOT EXISTS C(
				pk NUMBER PRIMARY KEY,
				ht NUMBER,
				tt NUMBER,
				ot NUMBER,
				filler CHAR(247), 
			 )''')

# Clear previous data; Insert stats into A
c.execute('DELETE FROM A')
c.execute('VACUUM')
c.executemany('INSERT INTO A(pk, ht, tt, ot, filler) VALUES (?,?,?,?)', stats)

# Shuffle stats
# Clear previous data; Insert stats into A
random.shuffle(stats)
c.execute('DELETE FROM benchmark_rand')
c.execute('VACUUM')
c.executemany('INSERT INTO benchmark_rand(theKey, columnA, columnB, filler) VALUES (?,?,?,?)', stats)

# Save execute and close connection
conn.commit()
conn.close()
