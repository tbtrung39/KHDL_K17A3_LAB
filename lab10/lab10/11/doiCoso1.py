def so_nguyen():
    n = int(input('Nhập vào một số nguyên: '))
    print(f'Số nguyên vừa nhập là: {n}')
    return n
def chuyen_doi_nhi_phan(n):
    nhi_phan = bin(n)[2:]
    print(f'Số {n} trong hệ nhị phân là: {nhi_phan}')
def chuyen_doi_bat_phan(n):
    bat_phan = oct(n)[2:]
    print(f'Số {n} trong hệ bát phân là: {bat_phan}')
def chuyen_doi_thap_luc_phan(n):
    thap_luc_phan = hex(n)[2:]
    print(f'Số {n} trong hệ thập lục phân là: {thap_luc_phan}')