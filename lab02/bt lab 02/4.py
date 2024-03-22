a = int(input("Nhập vào một số nguyên có 3 chữ số: "))
dem = len(str(a))
if dem >= 3:
    tinh_so = a // 100 % 10
else:
    tinh_so = 0
print(f"Chữ số hàng trăm của số {a} là: {tinh_so}")