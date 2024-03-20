n= int(input("nhap so lan tung xuc sac: "))
xac_suat = (1-(1-1/216)**n)**3
print(f"xác suất khi tung {n} lần 3 xúc sắc có ít nhất 1 lần cả 3 ra 6 la: {round(xac_suat,2)}")
