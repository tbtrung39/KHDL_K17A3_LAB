import random
so_chia_het = [so for so in range(201) if so % 5 == 0 and so % 7 == 0]
if so_chia_het:
    so_ngau_nhien = random.choice(so_chia_het)
    print(f"Số ngẫu nhiên chia hết cho cả 5 và 7 từ 0 đến 200 là: {so_ngau_nhien}")
else:
    print("Không có số nào chia hết cho cả 5 và 7 từ 0 đến 200.")
