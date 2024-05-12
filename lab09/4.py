def cac_hoan_vi(so):
    a = []
    hoan_vi(so, 0, a)
    return a

def hoan_vi(so, x, a):
    if x == len(so):
        a.append(so[:]) 
    else:
        for i in range(x, len(so)):
            so[i], so[x] = so[x], so[i]  
            hoan_vi(so, x + 1, a)  
            so[i], so[x] = so[x], so[i] 
n = int(input("Nhập vào số tự nhiên n: "))
so = list(range(1, n + 1))
a = cac_hoan_vi(so)
print("Tất cả các hoán vị của dãy [1, 2, ..., {}] là:".format(n))
for m in a:
    print(m)
