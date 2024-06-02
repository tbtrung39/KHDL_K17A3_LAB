lst = []
n = int(input("Nhập số phần tử n: "))
for i in range(1,n+1):
    lst.append(i)
result = map(lambda x: x ** 2, lst)
print(list(result), "là 1 list chứa bình phương các số hạng thuộc list trên")