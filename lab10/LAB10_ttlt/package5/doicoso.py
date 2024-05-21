def so_nguyen():
    n = int(input('Nhap vao mot so nguyen:  '))
    print(f"so vua nhap lai: {n}")
    return n
def chuyen_doi_nhi_phan(n):
    nhi_phan = bin(n)[2:]
    print(f"So {n} trong he nhi phan la: {nhi_phan}")
def chuyen_doi_bat_phan(n):
    bat_phan = oct(n)[2:]
    print(f"So {n} trong he bat phan la: ")
def chuyen_doi_thap_luc_phan(n):
    thap_luc_phan = hex(n)[2:]
    print(f"So {n} trong he thap luc phan la: {thap_luc_phan}")   
         