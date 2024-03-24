Diem = float(input("Nhập điểm học lực của học sinh là: "))
if Diem >= 0 and Diem <= 3:
    print("Loại kém")
elif Diem == 4:
    print("Loại yếu")
elif Diem >= 5 and Diem <= 6:
    print("Loại trung bình")
elif Diem >= 7 and Diem <= 8:
    print("Loại khá")
elif Diem >= 9 and Diem <= 10:
    print("Loại giỏi")