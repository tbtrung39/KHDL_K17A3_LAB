def qly(ma_hang,ten_hang,don_vi,don_gia,so_luong,thanh_tien,thue_vat):
    list = [ma_hang, ten_hang, don_vi, don_gia, so_luong, thanh_tien, thue_vat]
    new_list = list.sort(reverse=True, key= thue_vat)
    print(new_list)
