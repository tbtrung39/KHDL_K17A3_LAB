
van_ban=input("Nhập đoạn văn bản: ")
tu_trong_van_ban=van_ban.split()
tu_don=input("Nhập từ đơn: ")
so_lan_xuat_hien=0
for tu in tu_trong_van_ban:
    if tu.lower()==tu_don.lower():
        so_lan_xuat_hien+=1
print("Số lần từ '{}' xuất hiện trong đoạn văn bản là: {}".format(tu_don,so_lan_xuat_hien))
