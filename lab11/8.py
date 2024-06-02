import libs.xu_ly_thong_tin_nhanvien as xltt
import time as t
l=[]
def menu():
    print("-" * 60)
    print("CHƯƠNG TRÌNH QUẢN LÝ NHÂN VIÊN")
    print("-" * 60)
    print("1. Mở file danh sách nhân viên")
    print("2. Nhập thông tin nhân viên")
    print("3. Tính lương nhân viên")
    print("4. Lưu danh sách")
    print("5. Sắp xếp các nhân theo thứ tự giảm dần của thực lĩnh")
    print("6. Thoát chương trình!")
    print("-" * 60)
    print('\x1b[34m')
    choice = int(input("Chọn chức năng: "))
    while choice not in [1, 2, 3, 4, 5, 6]:
        print("Giá trị không hợp lệ ")
        choice = int(input("Chọn lại chức năng: "))
    print('\x1b[0m')
    return choice
while True:
    c = menu()
    if c == 1:
        xltt.doc_file(l)
    if c == 2:
        xltt.nhap_thong_tin_hs(l)
    if c == 3:
        xltt.Tinh_luong(l)
    if c == 4:
        xltt.luu_du_lieu(l)
    if c == 5:
        xltt.sap_xep(l)
        t.sleep(3)
    if c == 6:
        break
