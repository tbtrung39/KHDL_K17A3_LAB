S = 0
i = 1
a = 1
while True:
    S += a * 1/i
    a *= -1
    i += 1
    if abs(1/i) < 0.0001:
        break
print("Tổng của dãy là:", S)


S = 0
i = 1
while i <= 10:  
    S += 1 / (i * (i + 1))
    i += 1
print("Tổng của chuỗi S là:", S)



S = 0
i = 2
while True:
    a = 1 / (i ** 0.5)  
    if a < 0.000001: 
        break
    S += a  
    i += 1  
print("Tổng của dãy số là:", S)


