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
data = readcsv('data/guns.csv')
header = data[0]
data = data[1:]

#Manipulate
gender_counts = {}
race_counts = {}
genders = [row[5] for row in data]
races = [row[7] for row in data]

for gender in genders:
    if gender in gender_counts:
        gender_counts[gender] += 1
    else:
        gender_counts[gender] = 1

for race in races:
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1        

#Analysis
pp.pprint(header)
pp.pprint(gender_counts)
pp.pprint(race_counts)

#Conclusion
'''
Gun deaths in the US seem to disproportionately affect men vs women. 
They also seem to disproportionately affect minorities, 
although having some data on the percentage of each race in the overall US population would help.
There appears to be a minor seasonal correlation, with gun deaths peaking in the summer and declining 
in the winter. It might be useful to filter by intent, to see if different categories of intent
have different correlations with season, race, or gender.
'''