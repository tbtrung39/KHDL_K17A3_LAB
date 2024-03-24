a = int(input("Nhập số nguyên a: "))
if a < 100:
    print("0")
else:
    b = (a //100)%10
    print(f"{a} có chữ số hàng trăm là {b}")