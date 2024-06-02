def loai_bo_ky_tu(ky_tu):
    ky_tu_hop_le = set('0123456789ABCDEF')
    return ''.join(c for c in ky_tu if c in ky_tu_hop_le)

def co_so_chuoi_so(chuoi_so):
    if all(c in '01' for c in chuoi_so):
        return 2
    elif all(c in '01234567' for c in chuoi_so):
        return 8
    elif all(c in '0123456789ABCDEF' for c in chuoi_so):
        return 16
    else:
        return "Chuỗi số không hợp lệ"

def chuyen_doi_co_so(chuoi_so, co_so):
    return int(chuoi_so, co_so)

