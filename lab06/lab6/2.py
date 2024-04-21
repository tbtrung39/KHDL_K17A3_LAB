n=int(input("Nhập số phần tử của danh sách:"))
ds=[]
for i in range(0,n):
    phan_tu=int(input(f"Nhập phần tử thứ {i + 1} :"))
    ds.append(phan_tu)
ds_coppy=ds.copy()
max_1= max(ds_coppy)
ds_coppy.remove(max_1)
max_2= max(ds_coppy)
c=ds_coppy.index(max_2)
print(f"Giá trị lớn thứ 2: {max_2}")
print(f"Vị trí của số lớn thứ 2 là : {c}")

sum_sl=0
max_sl=0
for sl in ds :
    if sl > 0 :
        sum_sl+=1
        max_sl=max(max_sl,sum_sl)
    else:
        sum_sl = 0 
print(f"Số lượng các số dương liên tiếp nhiều nhất là:{max_sl}")

max_sum= 0
max_sl = 0
sl_ht= 0
sum_ht = 0
for sl in ds :
    if sl > 0 :
        sl_ht +=1
        sum_ht += sl
        max_sum=max(max_sum,sum_ht)
    else:
        sl_ht = 0
        sum_ht = 0

    if sum_ht == max_sum:
        max_sl = max(max_sl,sl_ht)
print(f"Số lượng các số dương liên tiếp có tổng lớn nhất là: {max_sl}")