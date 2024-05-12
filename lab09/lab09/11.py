def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * double_factorial(n - 2)

def sum_double_factorial(n):
    if n <= 1:
        return double_factorial(n)
    else:
        return double_factorial(n) + sum_double_factorial(n - 2)

n = int(input('Nhập số n: '))
print(f'Kết quả của tổng giai thừa kép là: {sum_double_factorial(n)}')
