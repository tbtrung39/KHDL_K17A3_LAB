
x=int(input('nhập x: '))
y=int(input('nhập y: '))
list_cha =[]
for i in range(x):
    list_con=[]
    for j in range(y):
        kq=i*j
        list_con.append(kq)
    list_cha.append(list_con)
print(list_cha)
