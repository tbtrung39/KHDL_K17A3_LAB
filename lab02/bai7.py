while True:   
    diem = float(input("Nhập điểm tổng kết: "))
    if diem < 0 or diem > 10:
        print("Điểm bạn nhập không đúng. Yêu cầu nhập lại !")
    elif 0 <= diem < 4.0:
        print("Loại kém")
    elif 4.0 <= diem < 5.0:
        print("Loại Yếu")
    elif 5.0 <= diem < 7.0:
        print("Loại Trung Bình")
    elif 7.0 <= diem < 9.0:
        print("Loại Khá")
    else:
        print("Loại Giỏi")
    break