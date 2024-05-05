def value(x):
    return x + 1

try:
    so = int(input("Nhập số nguyên: "))
    so_ke_tiep = value(so)
    print(f"Số kế tiếp của {so} là {so_ke_tiep}")
except ValueError:
    print("Vui lòng chỉ nhập số nguyên.")
