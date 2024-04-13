m=int(input("Nhập số hàng m: "))
n=int(input("Nhập số hàng n: "))
A=[]
for i in range(m):
    hang=[]
    for j in range(n):
        a_ij=int(input(f"Nhập phần tử a_{i+1}{j+1}: "))
        hang.append(a_ij)
    A.append(hang)
tong=sum(sum(hang) for hang in A)
print("Ma trận A: ")
for hang in A:
    print(hang)
print("Tổng các phần tử của ma trận A:", tong)
