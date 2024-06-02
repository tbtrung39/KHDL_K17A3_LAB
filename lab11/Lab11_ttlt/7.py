import csv
a=[]
with open(r"lab11\m_nums.txt","r") as m:
    mread=csv.reader(m)
    mlist=list(mread)


with open(r"lab11\n_nums.txt","r") as n:
    nread=csv.reader(n)
    nlist=list(nread)

for i in mlist:
    for j in nlist:
        if i==j:
            a.append(i)

with open(file="lab11\sochung.txt",mode="a") as openfiles:
    write=csv.writer(openfiles)
    for i in a:
        write.writerow(i)
        