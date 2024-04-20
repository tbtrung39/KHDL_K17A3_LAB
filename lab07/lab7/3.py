import random
n = int(input("Nhập vào ssó lượng các phần tử của tập hợp A: "))
A = set()
for _ in range(n):
    A.add(random.uniform(0,100))   
min = min(A)
max = max(A)
sum = sum(A)
print("phần tử lớn nhất trong tập hợp A là: ",max)
print("phần tử nhỏ nhất trong tập hợp A là: ",min)
print("tổng các phần tử trong tập hợp A là: ",sum)