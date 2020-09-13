import sys
import os
import pandas

if os.path.exists('files/data.csv'):
    with open('files/data.csv', 'r') as csv_file:
        csv_content = pandas.read_csv(csv_file, ',', header=0, names=('station 1', 'station 2'))
        print(csv_content)
        print(csv_content.mean()['station 1'])
        
else:
    print('no such file appeared')    

