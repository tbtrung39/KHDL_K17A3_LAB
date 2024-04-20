list1 = [1, 2, 3, 4, 5]
list2 = ['10 điểm ', '10 điểm ', '10 điểm', '10 điểm', ' 10 triệu điểm']
tu_dien = {}
for i in range(len(list1)):
    tu_dien[list1[i]] = list2[i]
print(tu_dien)