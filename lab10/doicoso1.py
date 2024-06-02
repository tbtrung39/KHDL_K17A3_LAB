
def nhap_so():
    try:
        so_nguyen = int(input("Nhập vào một số nguyên: "))
        return so_nguyen
    except ValueError:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số nguyên.")
        return nhap_so()
def chuyen_doi_nhi_phan(so):
    return bin(so)
def chuyen_doi_bat_phan(so):
    return oct(so)
def chuyen_doi_thap_luc_phan(so):
    return hex(so)
def hien_thi_ket_qua(so):
    print(f"Số đã nhập: {so}")
    print(f"Hệ nhị phân: {chuyen_doi_nhi_phan(so)}")
    print(f"Hệ bát phân: {chuyen_doi_bat_phan(so)}")
    print(f"Hệ thập lục phân: {chuyen_doi_thap_luc_phan(so)}")
