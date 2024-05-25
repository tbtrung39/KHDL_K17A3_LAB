import so_nguyen 
day_so=so_nguyen.sinh_day_so()
print("Day so la ngau nhien:", day_so)
nguyen_to_chia_het_cho_7=so_nguyen.liet_ke_nguyen_to_chia_het_cho_7(day_so)
print("Cac so nguyen to chia het cho 7 trong day: ", nguyen_to_chia_het_cho_7)
tong_so_le=so_nguyen.tinh_tong_so_le(day_so)
print("Tong cac so le trong day:", tong_so_le)
so_chinh_phuong=so_nguyen.kiem_tra_va_hien_thi_so_chinh_phuong(day_so)
if isinstance(so_chinh_phuong, list):
    print("Cac so chinh phuong trong day:", so_chinh_phuong)