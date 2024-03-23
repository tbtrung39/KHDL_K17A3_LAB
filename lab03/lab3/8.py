n = int(input('Nhập 1 giá trị: '))
tong1 = 0
tong2 = 0
tong3 = 0
for i in range(1,n+1):
    if i > 0:
        tong1 += i
        tong2 += (2*i+1)
        tong3 += 2*i
    else:
        break

print(f'a,{tong1}')
print(f'b,{tong2}')
print(f'c,{tong3}')