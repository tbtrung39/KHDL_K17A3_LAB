n = int(input("Nhập số cần kiểm tra: "))
so_nt = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        so_nt = False
        break

if so_nt:
    print(n, "là số nguyên tố.")
else:
    so_gan_nhat = n - 1
    while True:
        so_nt = True
        for i in range(2, int(so_gan_nhat**0.5) + 1):
            if so_gan_nhat % i == 0:
                so_nt = False
                break
        if so_nt:
            break
        so_gan_nhat -= 1
    
    print(n, "không phải là số nguyên tố. Số nguyên tố gần nhất là:", so_gan_nhat)