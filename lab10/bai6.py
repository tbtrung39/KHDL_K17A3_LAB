import package_6
chuoi = input("Nhập vào chuỗi cần lọc: ")
print(f"Chuỗi ban đầu là: {chuoi}")
chuoi_moi = package_6.dcs2.xoa_ki_tu(chuoi)
print(f"Chuỗi sau khi xóa là: {chuoi_moi}")
co_so = package_6.dcs2.phat_hien_he(chuoi)
print(f"Chuỗi {chuoi_moi} có hệ cơ số {co_so}")
if co_so == 2:
    co_so_2 = package_6.dcs2.he_2_sang_10(chuoi)
    print(f"Chuỗi {chuoi} đổi từ cơ số 2 sang cơ số 10 là {co_so_2}")
elif co_so == 8:    
    co_so_8 = package_6.dcs2.he_8_sang_10(chuoi)
    print(f"Chuỗi {chuoi} đổi từ cơ số 8 sang cơ số 10 là {co_so_8}")
elif co_so == 16:
    co_so_16 = package_6.dcs2.he_16_sang_10(chuoi)
    print(f"Chuỗi {chuoi} đổi từ cơ số 16 sang cơ số 10 là {co_so_16}")