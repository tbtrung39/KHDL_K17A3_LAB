list1 = input("Nhập danh sách các số khác nhau, cách nhau bằng dấu phẩy: ").split(',')
list2 = input("Nhập danh sách các tên, cách nhau bằng dấu phẩy: ").split(',')
tu_dien = {}
for i in range(min(len(list1), len(list2))):
    tu_dien[list1[i]] = list2[i]
print("Nội dung của từ điển:")
print(tu_dien)