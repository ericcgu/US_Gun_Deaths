'''
Extract the first row of data, and assign it to the variable headers.
Remove the first row from data.
Display headers.
Display the first 5 rows of data to verify that you removed the header row properly.
'''

import csv
import pprint
pp = pprint.PrettyPrinter(width=150) 

def readcsv(filename):
    with open(filename, 'r') as infile:
        data = list(csv.reader(infile))
        return data

data = readcsv('data/guns.csv')
header = data[0]
fiverowsof_data = data[1:6]
pp.pprint(header)
pp.pprint(fiverowsof_data)
