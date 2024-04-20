thi_sinh = {
    123: {'Họ và tên': 'Nguyễn Văn Thành', 'Điểm thi': 8},
    456: {'Họ và tên': 'Trần Thị Lan', 'Điểm thi': 7},
    789: {'Họ và tên': 'Lê Thị Ngọc', 'Điểm thi': 9}
}
def tra_cuu_diem_thi(so_bao_danh):
    if so_bao_danh in thi_sinh:
        print(f"Họ và tên: {thi_sinh[so_bao_danh]['Họ và tên']}, Điểm thi: {thi_sinh[so_bao_danh]['Điểm thi']}")
    else:
        ten = input("Nhập họ và tên của thí sinh: ")
        diem = int(input("Nhập điểm thi của thí sinh: "))
        thi_sinh[so_bao_danh] = {'Họ và tên': ten, 'Điểm thi': diem}
        print("Đã bổ sung thông tin của thí sinh.")
so_bao_danh = int(input("Nhập số báo danh của thí sinh: "))
tra_cuu_diem_thi(so_bao_danh)
print("\nTừ điển thông tin thí sinh sau khi tra cứu hoặc bổ sung:")
print(thi_sinh)