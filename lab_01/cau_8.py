# câu 8: VIẾT CHƯƠNG TRÌNH NHẬP VÀO X 
# TÍNH GIÁ TRỊ CỦA BIỂU THỨC SAU ( LÀM TRÒN ĐẾN SỐ THẬP PHÂN THỨ 2)
import math
x = int(input("nhập giá trị :"))
ket_qua_log = math.log(4,x) + math.log2(x)
print(f"kết quả biểu thức:{ket_qua_log}")