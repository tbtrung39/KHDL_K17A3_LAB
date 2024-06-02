import csv
count=0
list_cuc_tri=[]
with open("_in.dat","r") as dayso:
    listdayso=list(dayso)

for i in listdayso:
    dayso=i.split(",")

for i in dayso:
    if dayso[count]<dayso[count+1] and dayso[count]>dayso[count-1]:
        list_cuc_tri.append(i)
    if dayso[count]>dayso[count+1] and dayso[count]<dayso[count-1]:
        list_cuc_tri.append(i)

print(len(list_cuc_tri))
print(list_cuc_tri)