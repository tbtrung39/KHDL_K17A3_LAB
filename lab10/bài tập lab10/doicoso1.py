def in_ra_man_hinh(a):
    return a

def doi_nhi_phan(a):
    if a == 0:
        return "0"
    
    nhi_phan = ""
    while a > 0:
        so_tra_ve = a % 2
        nhi_phan = str(so_tra_ve) + nhi_phan
        a = a // 2
    
    return nhi_phan

def doi_bat_phan(a):
    if a == 0:
        return "0"
    
    bat_phan = ""
    while a > 0:
        so_tra_ve = a % 8
        bat_phan = str(so_tra_ve) + bat_phan
        a = a // 8
    
    return bat_phan
