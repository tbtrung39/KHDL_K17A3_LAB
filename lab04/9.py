n = int(input("Nhập một số: "))
a = 0
while n > 0:
    b = n % 10  
    a += b      
    n //= 10      
print("Tổng các chữ số của số vừa nhập là:", a)
