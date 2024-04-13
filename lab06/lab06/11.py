import random
#ý 1
n = int(input("Nhập số lượng phần tử của danh sách: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
print("Danh sách A:", A)
#ý 2
B= [i for i in A if i % 3 == 0 and i % 5 !=0 ]
print("danh sach B: ",B)
#ý 3
C = [i**2 for i in A]
print("danh sach C:", C)
#ý 4
D = random.choices([i for i in A if i % 3 ==0], k=n)
print("Danh sach D:",D )