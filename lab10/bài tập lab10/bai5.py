a = int(input("Nhập số nguyên:"))

import doicoso1
print(doicoso1.in_ra_man_hinh(a))

print(f'Nhị phân của {a} là:', end = " ")
print(doicoso1.doi_nhi_phan(a))

print(f'Bát phân của {a} là:', end = " ")
print(doicoso1.doi_bat_phan(a))