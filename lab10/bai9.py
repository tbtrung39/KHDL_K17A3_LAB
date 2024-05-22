import package_9
danh_sach_hang_hoa = []
so_luong_mat_hang = int(input("Nhập số lượng mặt hàng: "))
while so_luong_mat_hang <=0:
    so_luong_mat_hang = int(input("Số lượng mặt hàng không hợp lệ, hãy nhập lại: "))
for mat_hang in range (so_luong_mat_hang):
    hang_hoa_moi = package_9.ql.them_thong_tin()
    danh_sach_hang_hoa.append(hang_hoa_moi) 
print("Danh sách hàng hóa trước khi sắp xếp là:")
package_9.ql.in_danh_sach(danh_sach_hang_hoa)
danh_sach_sau_sap_xep = package_9.ql.sap_xep(danh_sach_hang_hoa)
print("Danh sách hàng hóa sau khi sắp xếp là:")
package_9.ql.in_danh_sach(danh_sach_sau_sap_xep)