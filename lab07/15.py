list1 = [1, 2, 3, 4, 5]  
list2 = ['Tran', 'Van', 'Tinh', 'Dep', 'Trai']  

result_dict = {f'<{list1[i]}>': f'<{list2[i]}>' for i in range(len(list1))}
print(result_dict)