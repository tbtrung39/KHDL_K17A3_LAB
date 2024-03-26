diem = float(input("Nhập điểm của học sinh: "))

if diem >= 0.0 and diem < 4.0:
    print("Học lực của học sinh: Loại Kém")
elif diem == 4.0:
    print("Học lực của học sinh: Loại Yếu")
elif diem >= 5.0 and diem < 7.0:
    print("Học lực của học sinh: Loại Trung bình")
elif diem >= 7.0 and diem < 9.0:
    print("Học lực của học sinh: Loại Khá")
elif diem >= 9.0 and diem <= 10.0:
    print("Học lực của học sinh: Loại Giỏi")
else:
    print("Điểm không hợp lệ, vui lòng nhập lại!")