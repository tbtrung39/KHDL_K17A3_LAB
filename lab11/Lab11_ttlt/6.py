import csv

with open("lab11\hbt.txt","r") as pd:
    pdread=csv.reader(pd)
    pdlist=list(pdread)

print(pdlist[0][0])
print(pdlist[2][0])
with open("lab11\hbt.txt","r") as bt:
    asd=bt.read()

print(asd)
dong1=pdlist[0][0].split(" ")
dong2=pdlist[1][0].split(" ")
dong3=pdlist[2][0].split(" ")
dong4=pdlist[3][0].split(" ")

def chuyendoi(lst):
    chuyendoiso=[]
    for i in lst:
        i=int(i)
        chuyendoiso.append(i)
    return chuyendoiso

def thayso(lst):
    for i in lst:
        if int(i) % 2 == 0:
            lst[lst.index(i)]=0
    return lst

thayso1=chuyendoi(dong1)
thayso2=chuyendoi(dong2)
thayso3=chuyendoi(dong3)
thayso4=chuyendoi(dong4)

print(thayso2)
thayso1=chuyendoi(thayso(dong1))
thayso2=chuyendoi(thayso(dong2))
thayso3=chuyendoi(thayso(dong3))
thayso4=chuyendoi(thayso(dong4))

print(thayso2)
def themso(lst):
    while len(lst) != 4:
        lst.append(0)
    return(lst)
thayso1=themso(thayso1)

print(thayso2)
a=[thayso1,thayso2,thayso3,thayso4]
print(a)
with open(file="lab11\ODD.txt",mode="a") as openfiles:
    write=csv.writer(openfiles)
    for i in a:
        write.writerow(i)
        