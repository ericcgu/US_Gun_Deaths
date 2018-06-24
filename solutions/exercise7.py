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
census = readcsv('data/census.csv')
header = census[0]
census_data = census[1:]

gun_deaths = readcsv('data/guns.csv')
header = gun_deaths[0]
gun_deaths_data = gun_deaths[1:]

#Manipulate
race_counts = {}
races = [row[7] for row in gun_deaths_data]

for race in races:
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1  

mapping  =  {
    "Asian/Pacific Islander" : 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}

race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

pp.pprint(race_per_hundredk)
