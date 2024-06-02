import csv
from operator import itemgetter

def docDS():
    danh_sach_sinh_vien = []
    with open("lab11\package_10\\files\ds_sinh_vien.csv", mode = "r", encoding = "utf-8") as file:
        reader = csv.reader(file)
        next (reader)
        for row in reader:
            SinhVien = {
                "Mã sinh viên": row[0],
                "Họ tên": row[1],
                "Điểm trung bình": row[2],
                "Điểm rèn luyện": row[3],
                "Điểm tích lũy": row[4],
            
            }
    return danh_sach_sinh_vien

def luuDS(danh_sach_sinh_vien):
    with open("lab11\package_10\\files\ds_sinh_vien.csv", mode = "w", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Mã sinh viên", "Họ tên", "Điểm trung bình", "Điểm rèn luyện", "Điểm tích lũy"])
        for sinh_vien in danh_sach_sinh_vien:
            writer.writerow([sinh_vien["Mã sinh viên"], sinh_vien["Họ tên"], sinh_vien["Điểm trung bình"], sinh_vien["Điểm rèn luyện"], sinh_vien["Điểm tích lũy"]])
            
def inDS(ds_sinh_vien):
    print ("{:<10} {:<25} {:<10} {:<15} {:<25}".format("Mã sinh viên", "Họ tên", "Điểm trung bình", "Điểm rèn luyên", "Điểm tích lũy"))
    for sinh_vien in ds_sinh_vien:
        print("{:<10} {:<25} {:<10} {:<15} {:<25}".format(sinh_vien["Mã sinh viên"], sinh_vien["Họ tên"], sinh_vien["Điểm trung bình"], sinh_vien["Điểm rèn luyện"], sinh_vien["Điểm tích lũy"]))  

def them_thong_tin_sinh_vien():
    ma_sv = input("Nhập mã sinh viên: ")
    ten_sv = input(f"Nhập tên sinh viên {ma_sv}: ")
    diem_trung_binh = float(input("Nhập điểm trung bình: "))
    while diem_trung_binh <0 or diem_trung_binh >10:
        diem_trung_binh = float(input("Điểm trung bình không hợp lệ, hãy nhập lại:"))
    diem_ren_luyen = float(input("Nhập điểm rèn luyện: "))
    while diem_ren_luyen <0 or diem_ren_luyen >10:
        diem_ren_luyen = float(input("Điểm rèn luyện không hợp lệ, hãy nhập lại"))
    diem_tl = (diem_trung_binh + diem_ren_luyen)/2
    SinhVien = {
        "Mã sinh viên": ma_sv,
        "Họ tên": ten_sv,
        "Điểm trung bình": diem_trung_binh,
        "Điểm rèn luyện": diem_ren_luyen,
        "Điểm tích lũy": diem_tl,
    }
    return SinhVien
def sap_xep(danh_sach_sinh_vien):
    diem_ren_luyen_tang_dan = sorted(danh_sach_sinh_vien, key = itemgetter('Điểm rèn luyện'))
    return diem_ren_luyen_tang_dan  

def in_sv_diem_tl_cao_nhat(danh_sach_sinh_vien):
    sinh_vien_cao_nhat = max(danh_sach_sinh_vien, key=itemgetter('Điểm tích lũy'))
    print("\nSinh viên có điểm tích lũy cao nhất:")
    print("{:<10} {:<25} {:<10} {:<15} {:<25}".format("Mã sinh viên", "Họ tên", "Điểm trung bình", "Điểm rèn luyện", "Điểm tích lũy"))
    print("{:<10} {:<25} {:<10} {:<15} {:<25}".format(sinh_vien_cao_nhat["Mã sinh viên"], sinh_vien_cao_nhat["Họ tên"], sinh_vien_cao_nhat["Điểm trung bình"], sinh_vien_cao_nhat["Điểm rèn luyện"], sinh_vien_cao_nhat["Điểm tích lũy"]))
    