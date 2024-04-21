
n = int(input("Nhập số tự nhiên n: "))


print("Các số nguyên tố đầu tiên:")
count = 0
num = 2
while count < n:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1
