n = int(input("Nhập số: "))
import math
if n <=0:
    print("Hãy nhập lại số nguyên dương")
else:
    check = True
    for i in range(2,int(math.sqrt(n)+1)):
        if n ==1 or n % i ==0:
            check = False
        break
if check:
    print(n, "là số nguyên tố")
else:
    a = n-1
    for j in range(2,int(math.sqrt(n)+1)):
        if a % j ==0:
            check = False
            break
        check = True
    if check:
        print("Số nguyên tố gần", n, "nhất là: ", a)
        