from libs import xulysinhvien as xlsv
def inMenu():
    print("CHƯƠNG TÌNH QUẢN LÝ SINH VIÊN")
    print("1. Nhập thông tin sinh viên")
    print("2. Lưu thông tin sinh viên")
    print("3. In ra màn hình thông tin danh sách sinh viên")
    print("4. Sắp xếp danh sách sinh viên theo điểm rèn luyện tặng dần")
    print("5. In thông tin sinh viên có điểm tích lũy cao nhất")

danh_sach_sinh_vien = xlsv.docDS()
tiep_tuc = "y"
while tiep_tuc.lower() == "y":
    inMenu()
    chuc_nang = input("Chọn chức năng: ")
    while chuc_nang not in ["1","2","3","4","5"]:
        chuc_nang = input("Chức năng không hợp lệ, hãy nhập lại: ")
        chuc_nang = int(chuc_nang)
    if chuc_nang == "1":
        SinhVien = xlsv.them_thong_tin_sinh_vien()
        if SinhVien:
            danh_sach_sinh_vien.append(SinhVien)
    elif chuc_nang == "2":
        xlsv.luuDS(danh_sach_sinh_vien)
    elif chuc_nang == "3":
        xlsv.inDS(danh_sach_sinh_vien)
    elif chuc_nang == "4":
        print("Danh sách nhân viên ban đầu là:")
        xlsv.inDS(danh_sach_sinh_vien)
        danh_sach_sap_xep = xlsv.sap_xep(danh_sach_sinh_vien)
        print("Danh sách nhân viên sau khi sắp xếp là:")
        xlsv.inDS(danh_sach_sap_xep)
    elif chuc_nang == "5":
        xlsv.in_sv_diem_tl_cao_nhat(danh_sach_sinh_vien)
    tiep_tuc = input("Bạn có muốn tiếp tục chương trình không (y/n): ")
    while tiep_tuc != "y" and tiep_tuc != "n":
        tiep_tuc = input("Giá trị không hợp lệ, hãy nhập lại (y/n): ")