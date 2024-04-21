thi_sinh_dict = {
    '001': {'họ tên': 'Nguyễn Văn A', 'điểm thi': 8.5},
    '002': {'họ tên': 'Trần Thị B', 'điểm thi': 7.2}
}
so_bao_danh = input("Nhập số báo danh của thí sinh: ")

if so_bao_danh in thi_sinh_dict:
    thong_tin = thi_sinh_dict[so_bao_danh]
    print(f"Họ tên: {thong_tin['họ tên']}, Điểm thi: {thong_tin['điểm thi']}")
else:
    ho_ten = input("Nhập họ tên thí sinh mới: ")
    diem_thi = float(input("Nhập điểm thi của thí sinh mới: "))
    thi_sinh_dict[so_bao_danh] = {'họ tên': ho_ten, 'điểm thi': diem_thi}
    print("Thông tin thí sinh đã được thêm vào.")