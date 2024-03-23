number = int(input("Nhập vào một số nguyên: "))
if number < 100:
    print("0")
else:
    hundreds_digit = (number // 100) % 10
    print(f"Chữ số hàng trăm của {number} là: {hundreds_digit}")

