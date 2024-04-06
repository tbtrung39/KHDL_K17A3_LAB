a = int(input("nhập bán kính:"))
b = int(input("nhập chiều cao:"))
pi = 3.14
dien_tich_xq = round((2*pi*a*b), 2)
dien_tich_tp = round((dien_tich_xq+2*pi*a**2), 2)
the_tich = round((pi*a**2*b), 2)
print(f"diện tích xq = {dien_tich_xq}, diện tích tp = {dien_tich_tp}, thể tích = {the_tich}")