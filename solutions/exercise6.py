'''
Count up how many times each item in the sex column occurs.
Assign the result to sex_counts.
Count up how many times each item in the race column occurs.
Assign the result to race_counts.
Display race_counts and sex_counts to verify your work, and see if you can spot any patterns.
'''

import csv
import pprint
import datetime
pp = pprint.PrettyPrinter(width=150) 

def readcsv(filename):
    with open(filename, 'r') as infile:
        data = list(csv.reader(infile))
        return data

#Extract
data = readcsv('data/census.csv')
header = data[0]
data = data[1:]

#Manipulate
pp.pprint(header)
pp.pprint(data)
