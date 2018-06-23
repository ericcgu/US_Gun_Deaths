'''
Use a list comprehension to extract the year column from data.
Because the year column is the second column in the data, you'll need to get the element at index 1 in each row.
Assign the result to the variable years.
Create an empty dictionary called year_counts.
Loop through each element in years.
If the element isn't a key in year_counts, create it, and set the value to 1.
If the element is a key in year_counts, increment the value by one.
Display year_counts to see how many gun deaths occur in each year.
'''

import csv
import pprint
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
years = [row[1] for row in data]
year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1

#Analysis
pp.pprint(year_counts)
