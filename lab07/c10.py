m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))
m = set(str(m))
n = set(str(n))
a = m.intersection(n)
for i in range(len(a)):
    result = sum(m.intersection(n))
print(result)
