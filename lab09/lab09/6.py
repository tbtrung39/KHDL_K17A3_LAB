import random

def random_hoan_vi(n, A=None):
    if A is None:
        A = list(range(1, n + 1))

    if not A: 
        return []

    a = random.choice(A)  
    A.remove(a)  
    return [a] + random_hoan_vi(n, A)  

def main():
    n = int(input('Nhập số tự nhiên n: '))
    result = random_hoan_vi(n)
    print(f'Hoán vị ngẫu nhiên của các số từ 1 đến {n} là: {result}')

main()
