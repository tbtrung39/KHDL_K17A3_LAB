import random
A=set()
B=set()
n=int(input('nhập số lượng phần tử tập hợp A:'))
m=int(input('nhập số lượng phần tử tập hợp B:'))
print('nhập phần tử cho tập hợp A:')
for _ in range(n):
    a=input('nhập phần tử:')
    A.add(n)
print('nhập phần tử cho tập hợp B:')
for _ in range(m):
    a=input('nhập phần tử:')
    B.add(m)
b=A.intersection(B)
print(' các phần tử chung của tập hợp A và B là:',b)