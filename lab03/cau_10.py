num = int(input("Nhập vào một số nguyên dương: "))

if num <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
else:
    divisor = 2
    has_factors = False
    while num > 1:
        if num % divisor == 0:
            if not has_factors:
                print(f"{num} = ", end="")
                has_factors = True
            print(divisor, end="")
            num //= divisor
            if num > 1:
                print(" × ", end="")
        else:
            divisor += 1

    if not has_factors:
        print(f"{num} là số nguyên tố.")
    else:
        print()
