def kiem_tra_cau_truc(chuoi):
    ky_tu_hop_le = "0123456789ABCDEF"
    danh_sach_chuoi = [ky_tu for ky_tu in chuoi if ky_tu in ky_tu_hop_le]
    return danh_sach_chuoi

def kiem_tra_he_co_so(so_co_so):
    ky_tu_hop_le = "0123456789ABCDEF"
    for ky_tu in so_co_so:
        if ky_tu in ky_tu_hop_le[:10]:
            print(so_co_so, "là hệ cơ số 10")
        elif ky_tu in ky_tu_hop_le[:2]:
            print(so_co_so, "là hệ cơ số 2")
        elif ky_tu in ky_tu_hop_le[:8]:
            print(so_co_so, "là hệ cơ số 8")
        elif ky_tu in ky_tu_hop_le:
            print(so_co_so, "là hệ cơ số 16")
        else:
            print("Không hợp lệ")

def chuyen_doi_nhi_phan_sang_thap_phan(nhi_phan):
    nhi_phan = int(nhi_phan)
    thap_phan, i = 0, 0
    while nhi_phan > 0:
        phan_du = nhi_phan % 10
        mu = phan_du * (2 ** i)
        thap_phan += mu
        nhi_phan //= 10
        i += 1
    return thap_phan

def chuyen_doi_bat_phan_sang_thap_phan(bat_phan):
    bat_phan = int(bat_phan)
    thap_phan, i = 0, 0
    while bat_phan > 0:
        phan_du = bat_phan % 10
        mu = phan_du * (8 ** i)
        thap_phan += mu
        bat_phan //= 10
        i += 1
    return thap_phan

def chuyen_doi_thap_luc_phan_sang_thap_phan(thap_luc_phan):
    chuyen_doi_chu_cai_sang_so = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    vi_tri = len(thap_luc_phan) - 1
    thap_phan = 0
    for ky_tu in thap_luc_phan:
        thap_phan += chuyen_doi_chu_cai_sang_so[ky_tu] * (16 ** vi_tri)
        vi_tri -= 1
    return thap_phan
