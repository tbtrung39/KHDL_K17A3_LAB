number = int(input("Nhập vào một số nguyên: "))
hundreds = number // 100 % 10
if hundreds>0 and hundreds<100:
    print("Chữ số hàng trăm của số đã nhập là: ", hundreds)
else:
    print("0")