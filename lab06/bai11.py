import random
#A
n = int(input("Nhập số phần tử của danh sách: "))
while n <= 0:
    n = int(input("Số phần tử của danh sách phải lớn hơn 0, vui lòng nhập lại: "))
A = []
B = []
C = []
D = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
    A.append(phan_tu)
print("Danh sách ban đầu là:",A)    
#B
for i in A:
    if i % 3 == 0 and i % 5 !=0:
        B.append(i)
print("Danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5 là:",B)
#C
for i in A:
    i = i ** 2
    C.append(i)
print("Danh sách C với các phần tử là bình phương của danh sách ban đầu là:", C)
#D
#D = random.choices([i for i in A if i % 3 ==0], k=n)
#print("Danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách ban đầu mà chia hết cho 3 là:",D )
for i in A:
    if i % 3 == 0:
        D.append(i)
        random.sample(D, k = len(D))
print("Danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách ban đầu mà chia hết cho 3 là:",D)
        