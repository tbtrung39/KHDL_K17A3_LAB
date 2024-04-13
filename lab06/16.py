x=int(input("Nhập x: "))
y=int(input("nhập y: "))4
list_cha=[]
for i in range(0, x):
    list_con=[]
    for j in range(0, y):
        kq=i*j
        list_con.append(kq)
    list_cha.append(list_con)
print(list_cha)