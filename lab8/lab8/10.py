def uoc_so(n):
    uoc_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc_list.append(i)
    return uoc_list

n = int(input('Nhập một số nguyên dương: '))

ket_qua = uoc_so(n)
print(f'Các ước của {n} là: {ket_qua}')