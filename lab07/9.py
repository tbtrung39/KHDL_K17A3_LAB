n = int(input("Nhập số tự nhiên n: "))
A = set()
for i in range(2, n + 1):
    if n % i == 0:  
        a = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                a = False
                break
        if a:
            A.add(i)
B = set()
for i in range(2, n):
    if i not in A:  
        a = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                a = False
                break
        if a:
            B.add(i)
print("Tập hợp A (các số nguyên tố là ước của n):", A)
print("Tập hợp B (các số nguyên tố nhỏ hơn n và không là ước của n):", B)
