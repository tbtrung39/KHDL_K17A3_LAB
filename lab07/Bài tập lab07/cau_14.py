dict = {}
for i in range(1, 101):
    nhi_phan = ""
    n = i
    while n > 0:
        a = n % 2
        nhi_phan = str(a) + nhi_phan
        n = n // 2
    dict[i] = nhi_phan
print(dict)
