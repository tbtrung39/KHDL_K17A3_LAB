a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
c = float(input("Nhập giá trị của c: "))
d = float(input("Nhập giá trị của d: "))
r = float(input("Nhập giá trị của r: "))
khoang_cach = ((c - a)**2 + (d - b)**2)**0.5
if khoang_cach < r:
    print("Điểm M nằm bên trong đường tròn.")
elif khoang_cach == r:
    print("Điểm M nằm trên đường tròn.")
else:
    print("Điểm M nằm bên ngoài đường tròn.")
