def power_of_a_number(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base ** exponent

base = int(input("Nhập số: "))
exponent = int(input("Nhập số mũ: "))
print(power_of_a_number(base,exponent), "là kết quả của phép lũy thừa")