def uoc_so(n):
    uoc = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc.append(i)
    return uoc

n = int(input("Nhập số nguyên n: "))

print("Các ước của", n, "là:", uoc_so(n))
