import random
import string
import sqlite3

# Build connection with db
conn = sqlite3.connect('/Users/yw7986/Desktop/my_db')
c = conn.cursor()

stats_a = []
stats_b = []
# generate data
def generator_a():
	''' GENERATE DATA '''
	stats = []
	index = 0
	while len(stats) < 5000000:
		# random 8 digits string
		str = ''.join([random.choice(string.ascii_lowercase) for i in range(8)])
		t = (index, random.randint(1, 5000000), random.randint(1, 5000000), str)
		stats.append(t)
		index +=1

	# more efficient
	# stats_a = [(i, random.randint(1, 5000000), random.randint(1, 5000000), str) for i in range(5000001)]
	return stats

#stats_a = generator_a()

def generator_b():
	''' GENERATE DATA '''
	ht = [i for i in range(0, 100000)] * 10
	tt = [i for i in range(0, 10000)]  * 100
	ot = [i for i in range(0, 1000)]   * 1000
	str = ''.join([random.choice(string.ascii_lowercase) for i in range(8)])
	stats = [(i + 1, ht[i], tt[i], ot[i], str) for i in range(0, 100000)]
	return stats

#stats_b = generator_b

# Create Tables
c.execute('''CREATE TABLE IF NOT EXISTS benchmark(
				theKey NUMBER PRIMARY KEY,
				columnA NUMBER,
				columnB NUMBER,
				filler CHAR(247)
			 )''')

c.execute('''CREATE TABLE IF NOT EXISTS benchmark_rand(
				theKey NUMBER PRIMARY KEY,
				columnA NUMBER,
				columnB NUMBER,
				filler CHAR(247)
			 )''')

# Clear previous data; Insert stats into benchmark
c.execute('DELETE FROM benchmark')
c.execute('VACUUM')
c.executemany('INSERT INTO benchmark(theKey, columnA, columnB, filler) VALUES (?,?,?,?)', stats_a)


# Shuffle stats
# Clear previous data; Insert stats into benchmark
random.shuffle(stats_a)
c.execute('DELETE FROM benchmark_rand')
c.execute('VACUUM')
c.executemany('INSERT INTO benchmark_rand(theKey, columnA, columnB, filler) VALUES (?,?,?,?)', stats_a)

# Save execute and close connection
conn.commit()
conn.close()                                                                                                                                                                                                  
