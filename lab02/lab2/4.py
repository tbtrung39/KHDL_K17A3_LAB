number = int(input("Nhập một số nguyên có 3 chữ số: "))

if number >= 100:
    print("Số hàng trăm là:", (number // 100) % 10)
else:
    print("Số hàng trăm là: 0")
