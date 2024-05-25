def doi_nhi_phan_sang_thap_luc_phan(nhi_phan):
    return hex(int(nhi_phan, 2))
def doi_thap_luc_phan_sang_nhi_phan(thap_luc_phan):
    return bin(int(thap_luc_phan, 16))[2:]