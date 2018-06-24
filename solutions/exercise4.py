'''
Use a list comprehension to create a datetime.datetime object for each row. Assign the result to dates.
The year column is in the second element in each row.
The month column is the third element in each row.
Make sure to convert year and month to integers using int().
Pass year, month, and day=1 into the datetime.datetime() function.
Display the first 5 rows in dates to verify everything worked.
Count up how many times each unique date occurs in dates. Assign the result to date_counts.
This follows a similar procedure to what we did in the last screen with year_counts.
Display date_counts.
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
dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day =13) for row in data]
date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
#Analysis
pp.pprint(header)
pp.pprint(dates[1:6])
pp.pprint(date_counts)

