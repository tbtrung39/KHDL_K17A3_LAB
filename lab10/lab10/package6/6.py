import doicoso2

chuoi = input("Nhập chuỗi kí tự: ")
print(doicoso2.kiem_tra_cau_truc(chuoi), "là chuỗi cuối cùng")

so_co_so = int(input("Nhập số: "))
print(doicoso2.kiem_tra_he_co_so(so_co_so))

nhi_phan = input("Nhập số nhị phân: ")
print(doicoso2.chuyen_doi_nhi_phan_sang_thap_phan(nhi_phan), "là kết quả chuyển sang hệ thập phân")

bat_phan = input("Nhập số bát phân: ")
print(doicoso2.chuyen_doi_bat_phan_sang_thap_phan(bat_phan), "là kết quả chuyển sang số thập phân")

thap_luc_phan = input("Nhập số thập lục phân: ")
print(doicoso2.chuyen_doi_thap_luc_phan_sang_thap_phan(thap_luc_phan), "là kết quả chuyển sang số thập phân")
