str1 = "Khoa, khoa hoc ung dung"
tu = str1.split()
for i in tu:
    i = i.replace(",", "")
    print(i)
