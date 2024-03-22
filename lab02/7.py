diem = float(input("nhập điểm :"))
if diem >= 0 and diem <= 3 :
    print("loại kém.")
elif diem == 4 :
    print("loại yếu.")
elif diem >= 5 and diem <= 6 :
    print("loại trung bình.")
elif diem >= 7 and diem <= 8 :
    print("loại khá.")
elif diem >= 9 and diem <= 10 :
    print("loại giỏi.")
else:
    print("chỉ nhập từ 0 đến 10.")                    