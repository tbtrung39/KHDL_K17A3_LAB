n = int(input("Nhập số: "))
import math
for i in range(2,n):
    if n % i ==0:
        break
    else:
        for i in range(i):
            print(i, "là các số nguyên tố <= ", n)