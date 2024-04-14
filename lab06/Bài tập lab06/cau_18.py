n = int(input("Nhập số hàng: "))
m = int(input("Nhập số cột: "))
A = []
for i in range(n):
    print(f"Hàng {i+1}")
    a=[]
    for j in range(n):
        a.append(int(input(f"Nhập A[{i+1}][{j+1}]: ")))
    A.append(a)
tong=0
for i in A:
    for j in i:
        tong+=j
print(f"Tổng của các phần tử trong ma trận: {tong}")
