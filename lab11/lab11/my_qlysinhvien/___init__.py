import csv

class SinhVien:
    def __init__(self, masv, hoten, diem_tb, diem_rl):
        self.masv = masv
        self.hoten = hoten
        self.diem_tb = diem_tb
        self.diem_rl = diem_rl
        self.diem_tl = (diem_tb + diem_rl) / 2

def nhap_danh_sach_sinh_vien():
    danh_sach_sinh_vien = []
    while True:
        masv = input("Nhập mã sinh viên (Nhập 'q' để kết thúc): ")
        if masv == 'q':
            break
        hoten = input("Nhập họ và tên sinh viên: ")
        diem_tb = float(input("Nhập điểm trung bình: "))
        diem_rl = float(input("Nhập điểm rèn luyện: "))
        sv = SinhVien(masv, hoten, diem_tb, diem_rl)
        danh_sach_sinh_vien.append(sv)
    return danh_sach_sinh_vien

def tinh_diem_tl(sv):
    return (sv.diem_tb + sv.diem_rl) / 2

def in_danh_sach_sinh_vien(danh_sach_sinh_vien):
    for sv in danh_sach_sinh_vien:
        print(f"Mã SV: {sv.masv}, Họ tên: {sv.hoten}, Điểm TB: {sv.diem_tb}, Điểm RL: {sv.diem_rl}, Điểm TL: {sv.diem_tl}")

def ghi_danh_sach_sinh_vien_vao_file(danh_sach_sinh_vien):
    with open('files/ds_sinhvien.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Mã SV", "Họ tên", "Điểm TB", "Điểm RL", "Điểm TL"])
        for sv in danh_sach_sinh_vien:
            writer.writerow([sv.masv, sv.hoten, sv.diem_tb, sv.diem_rl, sv.diem_tl])

def sap_xep_theo_diem_rl(danh_sach_sinh_vien):
    return sorted(danh_sach_sinh_vien, key=lambda sv: sv.diem_rl)

def in_sinh_vien_co_diem_tl_cao_nhat(danh_sach_sinh_vien):
    sv_max = max(danh_sach_sinh_vien, key=lambda sv: sv.diem_tl)
    print("Thông tin sinh viên có điểm TL cao nhất:")
    print(f"Mã SV: {sv_max.masv}, Họ tên: {sv_max.hoten}, Điểm TL: {sv_max.diem_tl}")

# Hàm main để chạy chương trình
def main():
    danh_sach_sinh_vien = nhap_danh_sach_sinh_vien()
    for sv in danh_sach_sinh_vien:
        sv.diem_tl = tinh_diem_tl(sv)
    print("\nDanh sách sinh viên:")
    in_danh_sach_sinh_vien(danh_sach_sinh_vien)
    ghi_danh_sach_sinh_vien_vao_file(danh_sach_sinh_vien)

    danh_sach_sinh_vien_sap_xep = sap_xep_theo_diem_rl(danh_sach_sinh_vien)
    print("\nDanh sách sinh viên sau khi sắp xếp theo điểm RL:")
    in_danh_sach_sinh_vien(danh_sach_sinh_vien_sap_xep)

    in_sinh_vien_co_diem_tl_cao_nhat(danh_sach_sinh_vien)

if __name__ == "__main__":
    main()