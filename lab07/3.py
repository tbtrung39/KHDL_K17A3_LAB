import random as rd
n=int(input('nhập vào số lượng phần tử của tập hợp A:'))
a=[rd.uniform(-10,10) for i in range(n)]
mi = min(a)
ma = max(a)
su = sum(a)
print('tập hợp A:',a)
print('phần tử nhỏ nhất :',mi)
print('phần tử lơn nhất :',ma)
print('tổng các phần tử :',su)