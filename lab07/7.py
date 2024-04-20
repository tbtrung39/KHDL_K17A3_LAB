import random
A_set=set(map(int,input("Nhập các phần tử của tập hợp A, cách nhau bởi dấu cách: ").split()))
B_set=set(map(int,input("Nhập các phần tử của tập hợp B, cách nhau bởi dấu cách: ").split()))
phan_tu_chung=A_set.intersection(B_set)
print("Các phần tử chung của tập hợp A và B là:", phan_tu_chung)