import random 
def lst():
    list = []
    for i in range(100):
        i = random.randint(1,100)
        list.append(i)
        print(list)
    for i in list:
        list_2 = []
        if i % 7 ==0:
            list_2.append(i)
            return list_2
    for j in list_2:
        sum = 0
        if j % 2 !=0:
            sum += j
            return j
    for k in range(1,10):
        list_3 = []
        if k**2 == j:
            list_3.append(j)
            return list_3
        elif k**2 !=j:
            print("không phải số chính phương")
            