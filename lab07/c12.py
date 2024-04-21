n = int(input("Nhập số nguyên n: "))
lst_1 = []
lst_2 = []
square = 1
for i in range(n):
    index_num = input("Nhập phần tử số {}: ".format(i))
    lst_1.append(index_num)

for i in range(n):
    square = i*i
    lst_2.append(square)

dict = {}
for i in range(n):
    dict[lst_1[i]] = lst_2[i]
print(dict)