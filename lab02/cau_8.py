#viết chương trình tính lương của nhân viên dựa theo thâm niên công tác
# lương = hệ số * lương căn bản => lương căn bản = 1350000 đồng
# nếu TNCT < 12 tháng : hệ số = 2.34
# nếu 12<= TNCT < 36 tháng : hệ số =3.33
# nếu 36 <= TNCT < 60 tháng: hệ số =3.66
# nếu TNCT >= 60 tháng : hệ số = 3.99
tham_nien_cong_tac = int(input("Nhập thâm niên công tác:"))
if tham_nien_cong_tac < 12:
    he_so = 2.34
elif tham_nien_cong_tac >= 12 and tham_nien_cong_tac < 36 :
    he_so = 3.33
elif tham_nien_cong_tac >= 36 and tham_nien_cong_tac < 60 :
    he_so = 3.66
elif tham_nien_cong_tac >= 60 :
    he_so = 3.99
luong_nhan_vien = tham_nien_cong_tac * he_so
print("Lương của nhân viên:",luong_nhan_vien)