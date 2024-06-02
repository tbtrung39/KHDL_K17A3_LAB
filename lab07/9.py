n = int(input("Nhập số tự nhiên n: "))

# Tạo tập hợp A và B
A = set()
B = set()

for i in range(2, n + 1):
    prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            prime = False
            break
    if prime:
        if n % i == 0:
            A.add(i)
        else:
            B.add(i)

print("Tập hợp A (các số nguyên tố là ước của n): ", A)
print("Tập hợp B (các số nguyên tố nhỏ hơn n và không là ước của n): ", B)
