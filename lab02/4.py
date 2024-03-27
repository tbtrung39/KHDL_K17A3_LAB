num = input("Nhập vào 1 số nguyên: ")
if len(num) >= 3:
    print("Chữ số hàng trăm của số là:", num[-3])
else:
    print("Không có chữ số hàng trăm, xuất ra 0")