def permutation(n):
    if n == 1:
        return [[1]]
    de_quy = permutation(n-1)
    a = []
    for x in de_quy:
        for i in range(len(x) + 1):
            b = x[:i] + [n] + x[i:]
            a.append(b)
    return a
n = int(input("Nhập giá trị n: "))
m = permutation(n)
print("Tất cả các hoán vị của dãy [1, 2, ..., {}] là:".format(n))
print(m)
