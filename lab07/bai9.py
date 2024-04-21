n = int(input("Nhập vào số tự nhiên n: "))
A = set()
B = set()

for i in range(2, n):
    is_prime = True
    if i > 1:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
    else:
        is_prime = False
        
    if is_prime:
        if n % i == 0:
            A.add(i)
        else:
            B.add(i)

print("Tập hợp của A bao gồm các số nguyên tố là ước của",n,"là:", A)
print("Tập hợp của B bao gồm các số nguyên tố nhỏ hơn",n,"và không là ước của",n,"là:",B)
