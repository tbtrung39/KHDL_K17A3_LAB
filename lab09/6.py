import random
def hoan_vi_ngau_nhien(n):
    A = list(range(1, n + 1))
    result = []
    while A:
        a = random.randint(0, len(A) - 1)
        b = A[a]
        result.append(b)
        A.pop(a)  
    return result
n = int(input("Nhập số tự nhiên n: "))
result = hoan_vi_ngau_nhien(n)
print("Hoán vị ngẫu nhiên của dãy từ 1 đến {} là:".format(n))
print(result)
