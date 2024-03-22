n = int(input("Nhap so n: "))
print("Cac so nguyen to be hon hoac bang n la: ")
for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num %i ==0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")