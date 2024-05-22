import package_8
n = int(input("Nhập kích thước của ma trận: "))
ma_tran = package_8.matranvuong.tao_ma_tran(n)
print("Ma trận vừa tạo là:")
package_8.matranvuong.in_ma_tran(ma_tran)

ma_tran_chuyen_vi = package_8.matranvuong.chuyen_vi_ma_tran(ma_tran)
print("Ma trận chuyển vị là:")
package_8.matranvuong.in_ma_tran_chuyen_vi(ma_tran_chuyen_vi)