list_tra_ve =[]
def f(n:int):
    for i in range(n):
        list_tra_ve.append(int(input(f"Nhập giá trị thứ {i+1}:")))
    return list_tra_ve

n = int(input("Nhập vào số số hạng:"))
list_a = f(n)
print(list_a)

list_b = list(map(lambda x : x*x, list_a))
print(list_b)
