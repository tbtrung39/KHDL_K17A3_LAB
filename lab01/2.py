# Nhập giá trị x từ bàn phím
x = float(input("Nhập giá trị của x: "))

# Tính giá trị của biểu thức
pi = 3.14
a = -x + ((x**2 + 4)**0.5)
b = (x**4 + 1)**0.5
f_x = a / b

# In giá trị của biểu thức, làm tròn đến số thập phân thứ hai
print("Giá trị của biểu thức là: {:.2f}".format(f_x))