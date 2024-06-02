a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# tính delta
delta = (b**2) - (4*a*c)

# kiểm tra các trường hợp của delta
if delta > 0:
    x1 = (-b - (delta)**0.5) / (2*a)
    x2 = (-b + (delta)**0.5) / (2*a)
    print("Phương trình có 2 nghiệm phân biệt là: {0} và {1}".format(x1, x2))
elif delta == 0:
    x12 = -b / (2*a)
    print("Phương trình có nghiệm kép là: ", x12)
else:
    print("Phương trình vô nghiệm")
