import random
import string
import sqlite3

# Build connection with db
conn = sqlite3.connect('/Users/yw7986/Desktop/my_db')
c = conn.cursor()

# generate data

def generator():
	''' GENERATE DATA '''
	ht = [i for i in range(0, 100000)] * 10
	tt = [i for i in range(0, 10000)]  * 100
	ot = [i for i in range(0, 1000)]   * 1000
	str = ''.join([random.choice(string.ascii_lowercase) for i in range(8)])
	stats = [(i + 1, ht[i], tt[i], ot[i], str) for i in range(0, 1000000)]
	return stats

#stats = generator()
stats = []
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

c.execute('DELETE FROM B')
c.execute('VACUUM')
c.executemany('INSERT INTO B(pk, ht, tt, ot, filler) VALUES (?,?,?,?)', stats)

c.execute('DELETE FROM C')
c.execute('VACUUM')
c.executemany('INSERT INTO B(pk, ht, tt, ot, filler) VALUES (?,?,?,?)', stats)



# Shuffle stats
# Clear previous data; Insert stats into A
#random.shuffle(stats)
#c.execute('DELETE FROM benchmark_rand')
#c.execute('VACUUM')
#c.executemany('INSERT INTO benchmark_rand(theKey, columnA, columnB, filler) VALUES (?,?,?,?)', stats)

# Save execute and close connection
conn.commit()
conn.close()
