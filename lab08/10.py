def uoc_so(n):
    so = []
    for i in range(1, n + 1):
        if n % i == 0:
            so.append(i)
    return so
try:
    n = int(input("Nhập một số nguyên dương n: "))
    if n <= 0:
        print("Vui lòng nhập số nguyên dương.")
    else:
        uoc_so = uoc_so(n)
        print(f"Các ước số của {n} là:", uoc_so)
except ValueError:
    print("Vui lòng chỉ nhập số nguyên.")
