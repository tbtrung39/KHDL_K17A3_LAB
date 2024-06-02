import math


def find_prime_factors(number):
    factors = []
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

with open('D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\lab11\\IN.dat', 'r') as file:
    data = file.readlines()

results = []

for line in data:
    number = int(line.strip())
    factors = find_prime_factors(number)
    results.append(factors)

with open('D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\\lab11\\out.dat', 'w') as file:
    for factors in results:
        file.write(' '.join(map(str, factors)) + '\n')

print('Kết quả đã được ghi vào tệp Out.dat.')