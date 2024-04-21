chuoi = input("Nhập vào một chuỗi: ")
tu_dien = {}
for i in range (len(chuoi)):
    for j in range(i, len(chuoi)):
        sub_chuoi = chuoi[i:j+1]
        if sub_chuoi in tu_dien:
            tu_dien[sub_chuoi]+=1
        else:
            tu_dien[sub_chuoi] = 1
print("Từ điển có các cặp (K, V) là:",tu_dien)                