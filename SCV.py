import csv

with open('hw.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

