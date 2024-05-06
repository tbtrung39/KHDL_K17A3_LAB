n = int(input("Nhập một số tự nhiên: "))

a = 0
num = 2
print(n, "số nguyên tố đầu tiên là:")

while a < n:
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)
        a += 1
    num += 1
    
