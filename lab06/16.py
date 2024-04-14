x =int(input('nhap gia tri cho x :'))
y = int(input('nhap gia tri cho y: '))
ma_tran_2_chieu=[]
for i in range(1,x+1):
    row = []
    for j in range(1,y +1):
        row.append(i*j)
    ma_tran_2_chieu.append(row)
print('ma tran 2 chieu duoc tao la: ')
for row in ma_tran_2_chieu:
    print(row  )