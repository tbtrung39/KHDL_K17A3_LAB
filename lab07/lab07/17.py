def nhap_thong_tin_sinh_vien():
    danh_sach_sinh_vien = {}
    so_luong_sv = int(input("Nhập số lượng sinh viên: "))
    
    for i in range(so_luong_sv):
        ma_sv = input(f"Nhập mã sinh viên thứ {i+1}: ")
        ten_sv = input(f"Nhập tên sinh viên thứ {i+1}: ")
        diem = round(float(input(f"Nhập điểm sinh viên {ten_sv}: ")))
        danh_sach_sinh_vien[ma_sv] = {"Tên": ten_sv, "Điểm": diem}
    
    return danh_sach_sinh_vien

def sap_xep_va_thong_ke_sinh_vien(danh_sach_sinh_vien):
    sorted_sinh_vien = sorted(danh_sach_sinh_vien.items(), key=lambda x: x[1]["Điểm"], reverse=True)
    
    diem_thong_ke = {}
    for ma_sv, sv in sorted_sinh_vien:
        diem = sv["Điểm"]
        if diem not in diem_thong_ke:
            diem_thong_ke[diem] = []
        diem_thong_ke[diem].append((ma_sv, sv["Tên"]))
    
    return diem_thong_ke

def in_danh_sach_sinh_vien(danh_sach_sinh_vien):
    for diem, ds_sv in danh_sach_sinh_vien.items():
        print(f"Điểm {diem}:")
        for ma_sv, ten_sv in ds_sv:
            print(f"Mã SV: {ma_sv}, Tên SV: {ten_sv}")
danh_sach_sinh_vien = nhap_thong_tin_sinh_vien()
diem_thong_ke = sap_xep_va_thong_ke_sinh_vien(danh_sach_sinh_vien)
in_danh_sach_sinh_vien(diem_thong_ke)
