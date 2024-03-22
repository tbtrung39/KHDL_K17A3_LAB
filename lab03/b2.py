n = int(input("Nhập giá trị của n: "))
print("Các số hoàn hảo nhỏ hơn", n, "là:")
for number in range(2, n):
    sum_of_divisors = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            sum_of_divisors += i
            if i != number // i:
                sum_of_divisors += number // i

    if sum_of_divisors == number:
        print(number)