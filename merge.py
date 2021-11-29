import csv
import pandas as stard


dataset1 = []
dataset2 = []
with open("bright_stars.csv",'r') as f:
    csv_reader =csv.reader(f)
    
    for row in csv_reader:
        dataset1.append(row)
        
with open("stars_converted.csv",'r') as f:
    csv_reader = csv.reader(f)
    
    for row in csv_reader:
        dataset2.append(row)

header1 = dataset1[0]
header2 = dataset2[0]

star_dataset1 = dataset1[1:]
star_dataset2 = dataset2[1:]

h = header1+header2

star_d =[]

for i in star_dataset1:
    star_d.append(i)
for j in star_dataset2:
    star_d.append(j)

with open("final.csv",'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(star_d)
