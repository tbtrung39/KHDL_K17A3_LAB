n = int(input("Nhập 1 số tự nhiên: "))
A = set()
B = set()
for i in range(2, n):
    so_nguyen_to = True
    for j in range(2, i):
        if i % j == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        if n % i == 0:
            A.add(i)
        else:
            B.add(i)
print(f"Các số nguyên tố là ước của {n} là: {A}")
print(f"Các số nguyên tố nhỏ hơn {n} và không là ước của {n} là: {B}")