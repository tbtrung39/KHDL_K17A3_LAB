
import qlyhanghoa
danh_sach_mat_hang=qlyhanghoa.nhap_danh_sach_mat_hang()
print("Danh sach mat hang truoc khi sap xep: ")
qlyhanghoa.in_danh_sach(danh_sach_mat_hang)
danh_sach_mat_hang_sap_xep=qlyhanghoa.sap_xep_theo_thue(danh_sach_mat_hang)
print("Danh sach mat hang sau khi sap xep theo thue VAT giam dan: ")
qlyhanghoa.in_danh_sach(danh_sach_mat_hang_sap_xep)
