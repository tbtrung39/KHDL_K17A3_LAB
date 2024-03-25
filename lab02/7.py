diem_tk=int(input("Nhập điểm tổng kết:"))
if diem_tk>0 and diem_tk<3:
    print("Xếp loại Kém")
elif diem_tk>4 and diem_tk<5:
    print("Xếp loại Yếu")
elif diem_tk>5 and diem_tk<6:
    print("Xếp loại Trung bình")
elif diem_tk>7 and diem_tk<8:
    print("Xếp loại Khá")
elif diem_tk>9 and diem_tk<10:
    print("Xếp loại Giỏi")
else:
    print("Vui lòng nhập lại")