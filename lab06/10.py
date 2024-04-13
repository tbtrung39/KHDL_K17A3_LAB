import random
so = [num for num in range(201)]
so_chia_het_5_va_7 = [num for num in so if num % 5 == 0 and num % 7 == 0]

# Nếu danh sách không rỗng, chọn ngẫu nhiên một số từ danh sách đó
if so_chia_het_5_va_7:
    n = random.choice(so_chia_het_5_va_7)
    print(f"Số ngẫu nhiên chia hết cho cả 5 và 7 từ 0 đến 200 là: {n}")
else:
    print("Không có số nào chia hết cho cả 5 và 7 từ 0 đến 200.")
