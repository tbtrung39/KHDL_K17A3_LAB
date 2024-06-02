def nhap_so():
    "Nhap vao mot so nguyen va in ra ket qua vua nhap"
    so=int(input("Nhap mot so nguyen: "))
    return so
def doi_sang_nhi_phan(so):
    "Chuyen doi so da nhap sang he nhi phan va in ra ket qua tren man hinh"
    nhi_phan=bin(so)
    return nhi_phan
def doi_sang_bat_phan(so):
    "Chuyen doi so da nhap sang he bat phan va in ra ket qua tren man hinh "
    bat_phan=oct(so)
    return bat_phan
def doi_sang_thap_luc(so):
    "Chuyen doi so da nhap sang he thap luc phan va in ra ket qua tren man hinh"
    thap_luc_phan=hex(so)
    return thap_luc_phan