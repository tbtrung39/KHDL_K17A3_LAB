import random
danh_sach=set(range(10))
tap_hop_A=set()
while len(tap_hop_A)<5:
    phan_tu=random.choice(list(danh_sach))
    tap_hop_A.add(phan_tu)
print("Tập hợp A:", tap_hop_A)