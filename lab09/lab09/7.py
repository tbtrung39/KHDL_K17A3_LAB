def find_solutions(n, x1, x2, x3):
    if x1 + x2 + x3 == n:
        return x1, x2, x3
    elif x1 + x2 + x3 < n:
        a = find_solutions(n, x1 + 1, x2, x3)
        b = find_solutions(n, x1, x2 + 1, x3)
        c = find_solutions(n, x1, x2, x3 + 1)
        
        return a, b, c

N = int(input('Nhập số N: '))
print(f'Các nghiệm của pt là: {find_solutions(N, 2, 2, 1)}')
