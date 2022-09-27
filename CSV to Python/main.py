import csv
from io import StringIO
import string

with open('testdaten.csv', 'r') as csvfile:
    file = StringIO(csvfile.read())
    spamreader = csv.reader(file, delimiter=';')
    
    for row in spamreader:
        i = 0
        for a in row:
            i+=1
            if(a == ''): # if empty
                a = 'EMPTY'
                row[i-1] = a
        print(' | '.join(row))