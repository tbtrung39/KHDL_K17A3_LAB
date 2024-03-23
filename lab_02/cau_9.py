# viết chương trình cho phép nhập số KW điện tiêu thụ
# KW : 0-> 100 : đơn giá 2000 đồng đồng/Kw
# KW : 101->200: đơn giá 2500 đồng/kw
# kw :201 -> 300 : đơn giá 3000 đồng/kw
# kw : > 300 : đơn giá 5000 đồng/kw
x = int(input("Nhập số KW điện tiêu thụ:"))
if x >= 0 and x <= 100 :
    a = 2000 * x
    print(f" {x} kw tính được số tiền điện là: {a} VNĐ")
elif x >= 101 and x <= 200:
    b = 2000*100 + 25000*(x-100)
    print(f" {x} kw tính được số tiền điện là: {b} VNĐ")
elif x >= 201 and x <= 300:
    c = 2000*100 + 2500*100 + 3000*(x - 200)
    print(f" {x} kw tính được số tiền điện là: {c} VNĐ")
elif x >= 300 :
    d = 2000*100 + 2500*100 + 3000* + 5000*(x -300)
    print(f" {x} kw tính được số tiền điện là: {d} VNĐ")

