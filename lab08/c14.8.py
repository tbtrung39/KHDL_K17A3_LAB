n = int(input("Nhập vào số hạng:"))
def f(n:int):
    list_tra_ve = []
    for i in range(n):
        list_tra_ve.append(int(input(f"Nhập giá trị thứ{i +1}:")))
        return list_tra_ve
a = f(n)
print(a)
b = list(map(lambda x: x*x,a))
print(b)