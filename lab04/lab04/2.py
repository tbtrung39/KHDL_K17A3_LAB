#a
n = int(input('Nhập vào một giá trị n: '))
s = 0
i = 1
while i<=n:
    if i%2 ==0:
        s-=1/i
    else:
        s +=1/i
    i+=1

print(f'Tổng của chuỗi là: {s}')

#b
n = int(input('Nhập vào một số nguyên : '))
s = 0
i = 1
while i <n:
    s += 1(i*(i+1))
    i += 1
print(f'Tổng của chuỗi là: {s}')

#c
n = int(input('Nhập vào một số nguyên n: '))
s = 0
i = 1
while i <=n:
    s += 1(i**0.5)
    i += 1
print(f'Tổng của chuỗi là: {s}')