list1 = input('Nhập danh sách các số khác nhau: ').split(',')
list2 = input('Nhập danh sách các tên: ').split(',')
dictionary = {}
for i in range(min(len(list1), len(list2))):
    dictionary[list1[i]] = list2[i]
print('Nội dung: ')
print(dictionary)