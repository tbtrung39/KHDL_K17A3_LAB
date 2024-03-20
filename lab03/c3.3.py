n = int(input("Nhập số n:"))
if n < 2:
    n = False
for i in range(2, int(n**0.5) + 1): 
    if n % i == 0: 
        n = False
        break

if n: 
    print(n, "là số nguyên tố.") 
else: 
    print(n, "không phải là số nguyên tố.")
