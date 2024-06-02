import csv
with open("lab11\dayso.dat","r") as dayso:
    listdayso=list(dayso)
print(listdayso)
for i in listdayso:
    dayso=i.split(",")
print(dayso)