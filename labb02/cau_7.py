# viết chương trình in ra màn hình học lực 
# điểm từ 0.0 -> 3.0 : loại kém
# điểm từ 4.0 :loại yếu
# điểm từ 5.0 -> 6.0 : loại trung bình
# điểm từ 7.0 -> 8.0 : loại loại khá
# điểm từ 9.0 -> 10.0 : loại giỏi
diem_01 = float(input("nhập điểm:"))
if diem_01 >= 0.0 and diem_01 <= 3.0 :
    print("loại kém")
elif diem_01 == 4.0:
    print("loại yếu")
elif diem_01 >= 5.0 and diem_01 <= 6.0:
    print("loại trung bình")
elif diem_01 >= 7.0 and diem_01 <= 8.0 :
    print(" loại khá")
elif diem_01 >= 9.0 and diem_01 <= 10.0 :
    print(" loại giỏi")
else:
    print("các kết quả khác")
 