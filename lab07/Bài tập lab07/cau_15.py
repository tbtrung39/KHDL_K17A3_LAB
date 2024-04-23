list1 = [1, 2, 3, 4, 5]
list2 = ["Đức", "Huy", "Kiên", "Sơn", "Vũ"]
dict = {}
if len(list1) != len(list2):
    print("Độ dài của hai danh sách không bằng nhau.")
else:
    for i in range(len(list1)):
        dict[list1[i]] = list2[i]
    print(dict)
