import csv
a=[]
with open("inp.txt","r") as dayso:
    listdayso=list(dayso)

for i in listdayso:
    dayso=i.split(",")

dayso.sort()
print(dayso)