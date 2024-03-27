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