list1=["a0","a1","a2","a3","a4"]
list2=["ten0","ten1","ten2","ten3","ten4"]
dictionary={list1[i]:list2[i] for i in range(len(list1))}   
for key, value in dictionary.items():
    print(key + ";",",".join(value))