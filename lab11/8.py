import csv

# Định nghĩa hàm để tính lương và phụ cấp
def tinh_luong(he_so_luong, chuc_vu):
    luong_co_ban = he_so_luong * 1490000
    phu_cap_chuc_vu = 0
    if chuc_vu == 'TP':
        phu_cap_chuc_vu = 1000000
    elif chuc_vu == 'PP':
        phu_cap_chuc_vu = 700000
    elif chuc_vu == 'NV':
        phu_cap_chuc_vu = 300000
        thuc_linh = luong_co_ban + phu_cap_chuc_vu
    return luong_co_ban, phu_cap_chuc_vu, thuc_linh

# Danh sách nhân viên
danh_sach_nhan_vien = []

# Menu chức năng
while True:
    print("1. Nhập danh sách nhân viên")
    print("2. Tính lương và in danh sách nhân viên")
    print("3. Sắp xếp và in danh sách nhân viên theo thực lĩnh giảm dần")
    print("4. Lưu danh sách nhân viên vào file ds_nhanvien.csv")
    print("5. Thoát")
    chon = input("Chọn chức năng: ")

    if chon == '1':
# Nhập thông tin nhân viên
        ma_nv = input("Nhập Mã NV: ")
        ten_nv = input("Nhập Tên NV: ")
        chuc_vu = input("Nhập Chức vụ (TP/PP/NV): ")
        he_so_luong = float(input("Nhập Hệ số lương: "))
        luong, pccv, thuc_linh = tinh_luong(he_so_luong, chuc_vu)
        danh_sach_nhan_vien.append({
        'Ma_NV': ma_nv,
        'Ten_NV': ten_nv,
        'Chuc_vu': chuc_vu,
        'He_so_luong': he_so_luong,
        'Luong': luong,
        'PCCV': pccv,
        'Thuc_linh': thuc_linh
                            })
    elif chon == '2':
# In danh sách nhân viên
        print("{:<10} {:<20} {:<10} {:<15} {:<15} {:<15} {:<15}".format('Ma_NV', 'Ten_NV', 'Chuc_vu', 'He_so_luong', 'Luong', 'PCCV', 'Thuc_linh'))
        for nv in danh_sach_nhan_vien:
            print("{:<10} {:<20} {:<10} {:<15} {:<15} {:<15} {:<15}".format(nv['Ma_NV'], nv['Ten_NV'], nv['Chuc_vu'], nv['He_so_luong'], nv['Luong'], nv['PCCV'], nv['Thuc_linh']))     
    elif chon == '3':
# Sắp xếp danh sách nhân viên theo thực lĩnh giảm dần
        danh_sach_nhan_vien.sort(key=lambda x: x['Thuc_linh'], reverse=True)
        print("Danh sách sau khi sắp xếp:")
        for nv in danh_sach_nhan_vien:
            print(nv)
    elif chon == '4':
# Lưu danh sách nhân viên vào file csv
        with open('ds_nhanvien.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Ma_NV', 'Ten_NV', 'Chuc_vu', 'He_so_luong', 'Luong', 'PCCV', 'Thuc_linh'])
            writer.writeheader()
        for nv in danh_sach_nhan_vien:
            writer.writerow(nv)
            print("Đã lưu danh sách nhân viên vào file ds_nhanvien.csv")

    elif chon == '5':
# Thoát chương trình
        break
