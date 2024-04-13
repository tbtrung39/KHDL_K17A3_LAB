import random
A=[random.randint(1,99999) for _ in range(1000)]
A_sorted=sorted(A)
print("Dãy A sau khi sắp xếp bằng hàm sorted():", A_sorted)


import random
A=[random.randint(1, 99999) for _ in range(1000)]
n=len(A)
for i in range(n-1):
    for j in range(0, n-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1]=A[j+1],A[j]
print("Dãy A sau khi sắp xếp không dùng hàm sorted():", A)