from libs import xu_ly_thong_tin as xl
def inMenu():
    print("CHƯƠNG TÌNH QUẢN LÝ NHÂN VIÊN")
    print("1. Nhập thông tin nhân viên")
    print("2. Lưu thông tin nhân viên")
    print("3. In ra màn hình thông tin danh sách nhân viên")
    print("4. Sắp xếp danh sách theo thực lĩnh giảm dần")

danh_sach_nhan_vien = xl.docDS()
tiep_tuc = "y"
while tiep_tuc.lower() == "y":
    inMenu()
    chuc_nang = input("Chọn chức năng: ")
    while chuc_nang not in ["1","2","3","4"]:
        chuc_nang = input("Chức năng không hợp lệ, hãy nhập lại: ")
        chuc_nang = int(chuc_nang)
    if chuc_nang == "1":
        NhanVien = xl.them_thong_tin_nhan_vien()
        if NhanVien:
            danh_sach_nhan_vien.append(NhanVien)
    elif chuc_nang == "2":
        xl.luuDS(danh_sach_nhan_vien)
    elif chuc_nang == "3":
        xl.inDS(danh_sach_nhan_vien)
    elif chuc_nang == "4":
        print("Danh sách nhân viên ban đầu là:")
        xl.inDS(danh_sach_nhan_vien)
        danh_sach_sap_xep = xl.sap_xep(danh_sach_nhan_vien)
        print("Danh sách nhân viên sau khi sắp xếp là:")
        xl.inDS(danh_sach_sap_xep)
    tiep_tuc = input("Bạn có muốn tiếp tục chương trình không (y/n): ")
    while tiep_tuc.lower() != "y" and tiep_tuc.lower() != "n":
        tiep_tuc = input("Giá trị không hợp lệ, hãy nhập lại (y/n): ") 