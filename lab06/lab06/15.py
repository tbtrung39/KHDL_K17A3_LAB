danh_sach=[]
while True:
    nhap=input("Nhập tuple (name, age, score), hoặc nhấn Enter để kết thúc:")
    if nhap=="":
        break
    danh_sach.append(tuple(nhap.split(',')))
if danh_sach: 
    danh_sach_sap_xep=sorted(danh_sach,key=lambda x: (x[0], int(x[1]), int(x[2])))
    print("Danh sách đã sắp xếp:")
    for item in danh_sach_sap_xep:
        print(item)
else:
    print("Không có dữ liệu để sắp xếp")