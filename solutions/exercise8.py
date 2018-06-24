'''
Extract the intent column using a list comprehension. The intent column is the fourth column in data.
Assign the result to intents.
Extract the race column using a list comprehension. The race column is the eighth column in data.
Assign the result to races.
Create an empty dictionary called homicide_race_counts
Check the value at position i in intents.
If the value at position i in intents is Homicide:
If the key race doesn't exist in homicide_race_counts, create it.
Add 1 to the value associated with race in homicide_race_counts.
When you're done, homicide_race_counts should have one key for each of the racial categories in data. The associated value should be the number of gun deaths by homicide for that race.
Perform the same procedure we did in the last screen using mapping on homicide_race_counts to get from raw numbers to rates per 100000.
Display homicide_race_counts to verify your work.
Write up your findings in a markdown cell.
Write up any next steps you want to pursue with the data in a markdown cell.
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
homicide_race_counts = {}
races = [row[7] for row in gun_deaths_data]
intents = [row[3] for row in gun_deaths_data]

for index, race in enumerate(races):
    if intents[index] == 'Homicide':
        if race not in homicide_race_counts:
           homicide_race_counts[race] = 0
        homicide_race_counts[race] += 1

mapping  =  {
    "Asian/Pacific Islander" : 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}

homicide_race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    homicide_race_per_hundredk[k] = (v / mapping[k]) * 100000

pp.pprint(homicide_race_per_hundredk)

#Findings
'''
Findings¶
It appears that gun related homicides in the US disproportionately affect people in the Black 
and Hispanic racial categories.
'''