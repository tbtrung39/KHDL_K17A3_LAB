def sum_of_n_numbers(n):
    if n <= 0:
        raise ValueError("n nguyen phai lon hon 0")
    S1 = sum(range(1, n + 1))
    S2 = sum([i**2 for i in range(1, n + 1)])
    return S1, S2
n = int(input("Nhap vao n: "))
try:
    S1, S2 = sum_of_n_numbers(n)
    print("Tong S1:", S1)
    print("Tong S2:", S2)
except ValueError as e:
    print("Loi:", e)
    