n = int(input("Nhập một số n: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10 
print("Tổng các chữ số của số vừa nhập là:", sum)