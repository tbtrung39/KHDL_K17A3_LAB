a = int(input("Nhập số nguyên dương thứ nhất: "))
b = int(input("Nhập số nguyên dương thứ hai: "))
while a<1:
    a = int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))
while b<1:
    b = int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))    
x, y = a, b
while b != 0:
    a, b = b, a % b
bcnn = x * y // a

print("Bội chung nhỏ nhất của hai số",x,"và",y,"là:", bcnn)    

a = int(input("Nhập số nguyên dương thứ nhất: "))
b = int(input("Nhập số nguyên dương thứ hai: "))
while a<1:
    a = int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))
while b<1:
    b = int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))
x, y = a, b        
while b:
    a, b = b, a%b
ucln = a
print("Ước chung lớn nhất của hai số",x,"và",y,"là: ",ucln)         