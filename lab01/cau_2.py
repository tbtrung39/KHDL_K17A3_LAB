# câu 2:VIẾT CHƯƠNG TRÌNH NHẬP VÀO X 
# TÍNH GIÁ TRỊ CỦA BIỂU THỨC DƯỚI ĐÂY (LÀM TRÒN ĐẾN SỐ THẬP PHÂN THỨ 2)

x = int(input("nhập giá trị:"))
ket_qua =(-x + (x**2 +4 )**1/2)/(x**4 + 1)**1/7
print(f"kết quả{ket_qua:.2f}")