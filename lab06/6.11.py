a =[]
while True:
    n = int(input("Nhập giá trị list(Nhập '0' để dừng): "))
    if n == 0:
        break
    a.append(n)
print(f'Danh sách list là: {a}')
a =[]
for i in range(1, n+1):
    if i%3 == 0 and i%5 != 0:
        h = a.append(i)
print('Danh sách các số chia hết cho 3 mà không chia hết cho 5 là:', end ='')
print(a)
#
for i in range(1, n+1):
    a.append(i**2)
    print(a, end ='')
#
import random
for i in range(1, n+1):
    if i%3 == 0:
        s = [random.randint(i) for _ in (1)]
        print(s)