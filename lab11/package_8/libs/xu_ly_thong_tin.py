import csv
from operator import itemgetter

def docDS():
    danh_sach_nhan_vien = []
    with open("lab11\package_8\\files\ds_nhan_vien.csv", mode = "r", encoding = "utf-8") as file:
        reader = csv.reader(file)
        next (reader)
        for row in reader:
            NhanVien = {
                "Mã nhân viên": row[0],
                "Tên nhân viên": row[1],
                "Chức vụ": row[2],
                "Hệ số lương": row[3],
                "Lương": row[4],
                "Phụ cấp chức vụ": row[5],
                "Thưc lĩnh": row[6]
            }
    return danh_sach_nhan_vien

def luuDS(danh_sach_nhan_vien):
    with open("lab11\package_8\\files\ds_nhan_vien.csv", mode = "w", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Mã nhân viên", "Tên nhân viên", "Chức vụ", "Hệ số lương", "Lương", "Phụ cấp chức vụ", "Thực lĩnh"])
        for nhan_vien in danh_sach_nhan_vien:
            writer.writerow([nhan_vien["Mã nhân viên"], nhan_vien["Tên nhân viên"], nhan_vien["Chức vụ"], nhan_vien["Hệ số lương"], nhan_vien["Lương"], nhan_vien["Phụ cấp chức vụ"], nhan_vien["Thực lĩnh"]])
            
def inDS(ds_nhan_vien):
    print ("{:<10} {:<25} {:<10} {:<15} {:<25} {:<10} {:<35}".format("Mã nhân viên", "Tên nhân viên", "Chức vụ", "Hệ số lương", "Lương", "Phụ cấp chức vụ", "Thực lĩnh"))
    for nhan_vien in ds_nhan_vien:
        print("{:<10} {:<25} {:<10} {:<15} {:<25} {:<10} {:<35}".format(nhan_vien["Mã nhân viên"], nhan_vien["Tên nhân viên"], nhan_vien["Chức vụ"], nhan_vien["Hệ số lương"], nhan_vien["Lương"], nhan_vien["Phụ cấp chức vụ"], nhan_vien["Thực lĩnh"]))  

def them_thong_tin_nhan_vien():
    ma_nv = input("Nhập mã nhân viên: ")
    ten_nv = input(f"Nhập tên nhân viên {ma_nv}: ")
    chuc_vu = input(f"Nhập chức vụ của nhân viên {ma_nv}: ")
    while chuc_vu.upper() not in ["TP", "PP", "NV"]:
        chuc_vu = input("Chức vụ không hợp lệ, hãy nhập lại: ")
    he_so_luong = int(input(f"Nhập hệ số lương của nhân viên {ma_nv}: "))
    while he_so_luong <=0:
        he_so_luong = int(input("Hệ số lương không hợp lệ, hãy nhập lại:"))
    luong = he_so_luong * 1490000
    phu_cap = 0
    if chuc_vu == "TP":
        phu_cap = 1000000
    elif chuc_vu == "PP":
        phu_cap = 700000
    elif chuc_vu == "NV":
        phu_cap = 300000
    thuc_linh = luong + phu_cap
    NhanVien = {
        "Mã nhân viên": ma_nv,
        "Tên nhân viên": ten_nv,
        "Chức vụ": chuc_vu,
        "Hệ số lương": he_so_luong,
        "Lương": luong,
        "Phụ cấp chức vụ": phu_cap,
        "Thực lĩnh": thuc_linh
    }
    return NhanVien
def sap_xep(danh_sach_nhan_vien):
    thuc_linh_giam_dan = sorted(danh_sach_nhan_vien, key = itemgetter('Thực lĩnh'))[::-1]
    return thuc_linh_giam_dan           