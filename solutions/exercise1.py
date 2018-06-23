'''
Read the dataset in as a list using the csv module.
Import the csv module.
Open the file using the open() function.
Use the csv.reader() function to load the opened file.
Call list() on the result to get a list of all the data in the file.
Assign the result to the variable data.
Display the first 5 rows of data to verify everything.
'''

import csv
import pprint

pp = pprint.PrettyPrinter(width=150) 

def readcsv(filename):
    with open(filename, 'r') as infile:
        data = list(csv.reader(infile))
        return data

pp.pprint(readcsv('data/guns.csv')[:5])

