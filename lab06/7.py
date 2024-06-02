list_ = [['mon',73],['tue', 89],['wed',95],['thu',103],['fri',115],['sat',128],['sun',120]]
for i in list_:
    print(i)
print(list_[2][1])    
#
print(len(list_))
list_.append(['random',150])
print(len(list_))
#
total_sale = 0
for i in list_:
    if i[0] in ['tue','sat','wed','sun']:
        total_sale += i[1]
print(total_sale)


    
    