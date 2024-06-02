def tinh_luong(he_so_luong):
    return he_so_luong * 1490000

def tinh_phu_cap(chuc_vu):
    if chuc_vu == 'TP':
        return 1000000
    elif chuc_vu == 'PP':
        return 700000
    elif chuc_vu == 'NV':
        return 300000

def tinh_thuc_linh(he_so_luong, chuc_vu):
    luong = tinh_luong(he_so_luong)
    phu_cap = tinh_phu_cap(chuc_vu)
    return luong + phu_cap
