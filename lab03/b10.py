n = int(input("Nhập số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    print("Phân tích thừa số nguyên tố của", n, "là:", end=" ")
    divisor = 2  
    while n > 1:
        if n % divisor == 0:  
            print(divisor, end=" ") 
            n //= divisor 
        else:
            divisor += 1  