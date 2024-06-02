import csv
a=[]
with open("lab11\inp.txt","r") as dayso:
    listdayso=list(dayso)

for i in listdayso:
    dayso=i.split(",")

dayso.sort()
print(dayso)