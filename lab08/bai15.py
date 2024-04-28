n = int(input("Nhập số phần tử của list: "))
lst = []
for i in range(n):
    lst.append(int(input("Nhập phần tử thứ {}: ".format(i+1))))
lst_le = list(map(lambda x: x**2, filter(lambda x: x%2 != 0, lst)))
print("List chứa bình phương các số lẻ: ", lst_le)