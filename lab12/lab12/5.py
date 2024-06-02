def sum_of_n_numbers(n):
    if n <= 0:
        raise ValueError('n phải là số dương.')
    
    S1 = 0
    S2 = 0
    for i in range(1, n + 1):
        S1 += i
        S2 += i**2
    
    return S1, S2

n = int(input('Nhập n: '))
try:
    S1, S2 = sum_of_n_numbers(n)
    print(f'S1 = {S1}')
    print(f'S2 = {S2}')
except ValueError as e:
    print(f'Lỗi: {e}')