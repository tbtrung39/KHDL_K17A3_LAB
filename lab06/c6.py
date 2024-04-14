# ý a
import random
A=[random.randint(1, 99999) for i in range(1000)]
print(A)
sorted(A)
print("Thứ tự tăng dần là :",sorted(A))
#ý b
import random
A=[random.randint(1, 99999) for i in range(1000)]
print(A)
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i] > A[j]:
            A[i],A[j] = A[j], A[i]
print(A)