def loai_bo_ky_tu_khong_hop_le(chuoi):
    ky_tu_hop_le="0123456789ABCDEF"
    chuoi_ket_qua=''.join(ky_tu for ky_tu in chuoi.upper() if ky_tu in ky_tu_hop_le)
    return chuoi_ket_qua
def bieu_dien_co_so(chuoi):
    chuoi=chuoi.upper()
    if all(ky_tu in "01" for ky_tu in chuoi):
        return 2
    elif all(ky_tu in "0123456789ABCDEF" for ky_tu in chuoi):
        return 16
    else:
        return -1