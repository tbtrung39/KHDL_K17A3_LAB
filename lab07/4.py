ds=[161,182,154,176,170,167,171,170,174,150,142,148,165,165,170,178,156,145,149,163,162,159,165,165,170,180,155,159,155,153,152,162,180,168,169,168,167,170]
print("Danh sách có:",len(ds),"sinh viên")
tong=0
for i in ds:
    tong+=i
print(f"Chiều cao trung bình của sinh viên là:{tong/len(ds)}")
set=set()
tong2=0
for j in ds:
    set.add(i)
    tong2+=j
print(set)
print(f"Chiều cao trung bình của nhóm là: {tong2/len(set)}")