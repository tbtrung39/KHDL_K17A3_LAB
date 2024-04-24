def f(n:int):
    list_tra_ve = []
    for i in range(n):
        list_tra_ve.append(int(input(f"nhập gtri thứ {i +1}: ")))
    return list_tra_ve

n = int(input("nhập số số hạng: "))
a = f(n)

print(a)

b = list(map(lambda x: x*x, a))
print(b)