class SinhVien:
    def __init__(self, ma_sinh_vien, ten, diem):
        self.ma_sinh_vien = ma_sinh_vien
        self.ten = ten
        self.diem = diem

    def __repr__(self):
        return f"Mã sinh viên: {self.ma_sinh_vien}, Tên: {self.ten}, Điểm: {self.diem}"

sinh_vien = []
for _ in range(int(input("Nhập số lượng sinh viên: "))):
    ma_sinh_vien = input("Nhập mã sinh viên (6 ký tự số): ")
    ten = input("Nhập tên sinh viên: ")
    diem = round(float(input("Nhập điểm sinh viên: ")))
    
    if 0 <= diem <= 10:
        sinh_vien.append(SinhVien(ma_sinh_vien, ten, diem))
    else:
        print("Điểm không hợp lệ. Vui lòng nhập giá trị từ 0 đến 10.")

sinh_vien.sort(key=lambda x: x.diem, reverse=True)

for sv in sinh_vien:
    print(sv)
