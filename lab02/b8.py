tham_nien_cong_tac = int(input("nhap vao tham nien cong tac( so thang): "))
if tham_nien_cong_tac < 12:
    he_so = 2.34
elif tham_nien_cong_tac >=12 and tham_nien_cong_tac <36:
    he_so = 3.33
elif tham_nien_cong_tac >=36 and tham_nien_cong_tac <60:
    he_so = 3.66
elif tham_nien_cong_tac >=60:
    he_so = 3.99
luong_can_ban = 1350000
luong = he_so*luong_can_ban
print(f"luong cua nhan vien la: {luong}dong")