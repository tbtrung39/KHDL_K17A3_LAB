import random
ds=[0,1,2,3,4,5,6,7,8,9]
ds_new=set()
for i in range(5):
    index=random.randint(0,len(ds)-1)
    ds_new.add(index)
print('Danh sách',ds)
print('Tập hợp A là :',ds_new)