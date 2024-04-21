import random

danh_sach = [num for num in range(201) if num % 5 == 0 and num % 7 == 0]
so_ngau_nhien=random.choice(danh_sach)
print("Danh sách các số ngẫu nhiên chia hết cho 5 và 7:", so_ngau_nhien)