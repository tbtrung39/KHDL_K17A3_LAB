n = int(input("Nhập một số tự nhiên: "))
A = set()
for i in range(2, n):
    so_nguyen_to = True
    for j in range(2, i):
        if i % j == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
            A.add(i)
print(f"Các số nguyên tố nhỏ hơn {n} là: {A}")
