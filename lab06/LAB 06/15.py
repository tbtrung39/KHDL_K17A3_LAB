n = int(input("Nhap so luong thong tin can sap xep: "))
danh_sach =[]
for i in range(n):
    ten = input("Nhap ten cho thong tin thu: ")
    tuoi = int(input("Nhap tuoi cho thong tin thu: "))
    diem = float(input("Nhap diem cho thong tin thu: "))
    danh_sach.append((ten,tuoi,diem))

sorted_danh_sach = sorted(danh_sach,key=danh_sach(0,1,2)) 
print("Danh sach sau khi sap xep:")
for item in sorted_danh_sach:
    print(item)   