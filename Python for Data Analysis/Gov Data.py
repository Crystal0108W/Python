path = 'Python for Data Analysis/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()

import json
records = [json.loads(line) for line in open(path)]
records[0]

#records[0]['a']
#print (records[0]['a'])

time_zone = [rec['tz'] for rec in records if 'tz' in rec] # Not all records has tz:timezone
time_zone[:10]

def get_counts(sequence):
    counts = {}
    for x in sequence: 
        if x in counts:
            counts[x] +=1
        else: 
            counts[x] =1
    return counts

get_counts(time_zone)

# Use Python standard library
from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] +=1
    return counts
get_counts2(time_zone)

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:] # change the order from descending to ascending

counts = get_counts(time_zone)
top_counts(counts)


# Use Python standard library
from collections import Counter
counts = Counter(time_zone)
counts.most_common(10)


from pandas import DataFrame, Series
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
frame = DataFrame(records)

frame
frame['tz'][:10]
tz_counts = frame['tz'].value_counts()
tz_counts[:10]

clean_tz = frame['tz'].fillna('Missing') #replace missing values
clean_tz[clean_tz == ''] = 'Unknown' # replace unknown values (empty strings)
tz_counts = clean_tz.value_counts()
temp = tz_counts[:10]
type(temp)
temp.plot(kind = "barh")
plt.show()

results = Series([x.split()[0] for x in frame.a.dropna()]) #splitoff the first token in the string
results[:5]
results.value_counts()[:8]

from pandas import DataFrame, Series
import numpy as np

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')

by_tz_os = cframe.groupby(['tz', operating_system]) # Group dataframe by 'tz' and the list of operating system
type(by_tz_os)
agg_counts = by_tz_os.size().unstack().fillna(0) # The group counts, analogous to the value_counts function above, can be computed using size. 
#This result is then reshaped into a table with unstack.
agg_counts[:10]

# Select the top overall time zones: 
indexer = agg_counts.sum(1).argsort() 
#.argsort() Perform an indirect sort along the given axis using the algorithm specified by the kind keyword. It returns an array of indices of the same shape as a that index data along the given axis in sorted order.
indexer[:10]
count_subset = agg_counts.take(indexer)[-10:] #use take to select the rows in that order and slice off the last 10 rows.
count_subset
count_subset.plot(kind = 'barh', stacked = True)
plt.show()

# Make it easier to see the percentage of Windows users, to normalize to sum to 1 then plot again. 
normed_subset = count_subset.div(count_subset.sum(1), axis = 0) #Floating division of dataframe and other, element-wise; axis = 0, index/for each row
normed_subset.plot(kind = "barh", stacked = True)
plt.show()
