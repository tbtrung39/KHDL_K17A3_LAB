tu_dien_nhi_phan = {}

for i in range(1, 101):
    tu_dien_nhi_phan[i] = bin(i)[2:] 

print("Từ điển các cặp (số, chuỗi nhị phân):")
print(tu_dien_nhi_phan)
