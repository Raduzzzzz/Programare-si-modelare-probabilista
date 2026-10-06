import random
import csv

studenti=[]
with open("studenti.csv", "r") as f:
    data = csv.reader(f)
    next(data)
    for row in data:
        studenti.append(row[1]+" "+row[2])

for student in random.sample(studenti, 3):
    print(student)



