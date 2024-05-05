def cac_so(so1, so2, so3):
    so_min = min(so1, so2, so3)
    so_max = max(so1, so2, so3)
    return so_min, so_max

try:
    so1 = int(input("Nhập số nguyên thứ nhất: "))
    so2 = int(input("Nhập số nguyên thứ hai: "))
    so3 = int(input("Nhập số nguyên thứ ba: "))
    
    so_min, so_max = cac_so(so1, so2, so3)
    print(f"Số nhỏ nhất là {so_min}, số lớn nhất là {so_max}")
except ValueError:
    print("Vui lòng chỉ nhập số nguyên.")
