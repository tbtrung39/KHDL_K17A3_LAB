def lap_phuong(so):
    return so ** 3

try:
    so = int(input("Nhập một số nguyên: "))
    cubed_value = lap_phuong(so)
    print(f"Giá trị lập phương của {so} là {cubed_value}")
except ValueError:
    print("Vui lòng chỉ nhập số nguyên.")
