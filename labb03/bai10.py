n = int(input("Nhập n: "))
for uoc_so in range(2, n + 1):
    if n % uoc_so == 0:
        a = uoc_so
        so_nt = True
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                so_nt = False
                break
        if so_nt:
            print("Thừa số nguyên tố của", n, "là:", a)




