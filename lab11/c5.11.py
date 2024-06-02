import csv
with open("lab11\phieu_diem.txt","r") as pd:
    pdread=csv.reader(pd)
    pdlist=list(pdread)

with open("lab11\sbd_ph.dat","r") as ph:
    phread=csv.reader(ph)
    phlist=list(phread)

with open("lab11\sbd_ten.dat","r") as ten:
    tenread=csv.reader(ten)
    tenlist=list(tenread)

print(len(pdlist[0]))