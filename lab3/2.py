n = int(input("Nhập một số nguyên dương n: "))
so_hoan_hao = []

for num in range(2, n):
    tong_cac_uoc = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            tong_cac_uoc += i
            if i != num // i:
                tong_cac_uoc += num // i

    if tong_cac_uoc == num:
        so_hoan_hao.append(num)

print(f"Các số hoàn hảo nhỏ hơn {n} là: {so_hoan_hao}")

