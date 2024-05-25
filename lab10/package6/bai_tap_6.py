import doicoso2
chuoi=input("Nhap mot chuoi ky tu: ")
chuoi_hop_le=doicoso2.loai_bo_ky_tu_khong_hop_le(chuoi)
co_so=doicoso2.bieu_dien_co_so(chuoi_hop_le)
if co_so in [2, 8, 16]:
    so_10=int(chuoi_hop_le, co_so)
    print(f"Chuoi {chuoi_hop_le} tu co so {co_so} sang co so 10 la: {so_10}")
else:
    print("Khong the xac dinh duoc co so cua chuoi")