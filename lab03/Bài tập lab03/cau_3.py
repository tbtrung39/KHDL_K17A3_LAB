num = int(input("Nhập một số nguyên dương: "))

if num > 1:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(num, "là số nguyên tố.")
else:
    lower_prime = num - 1
    while lower_prime > 1:
        is_lower_prime = True
        for i in range(2, int(lower_prime**0.5) + 1):
            if lower_prime % i == 0:
                is_lower_prime = False
                break
        if is_lower_prime:
            break
        lower_prime -= 1

    higher_prime = num + 1
    while True:
        is_higher_prime = True
        for i in range(2, int(higher_prime**0.5) + 1):
            if higher_prime % i == 0:
                is_higher_prime = False
                break
        if is_higher_prime:
            break
        higher_prime += 1

    closest_prime = lower_prime if abs(num - lower_prime) <= abs(num - higher_prime) else higher_prime
    print(num, "không phải là số nguyên tố. Số nguyên tố gần nhất là:", closest_prime)
