n = int(input("Nhập số: "))
set_A = set()
set_B = set()
sum_1 = 0
sum_2 = 0
# set A chứa số nguyên tố là ước của n , set B chứa số nguyên tố <n ko phải ước của n
for i in range(2,n):
    if n % i ==0 and n // i ==0:
        set_A.add(i)
for j in range(2,n-1):
    if n % j ==0 and n // j !=0:
        set_B.add(j)
print(set_A)
print(set_B)