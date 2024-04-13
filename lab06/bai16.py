x = int(input("nhap x: "))
y = int(input("nhap y: "))
list_c = []
for i in range(0,x):
    list_s = []
    for j in range(0,y):
        kq = i*j
        list_s.append(kq)
    list_c.append(list_s)
print(list_c)