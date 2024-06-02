def nhap_matran(N):
    matran = []
    for i in range(N):
        row = list(map(int, input("Nhập dòng thứ {} của ma trận: ".format(i+1)).split()))
        matran.append(row)
    return matran

def in_matran(matran):
    for row in matran:
        print(' '.join(map(str, row)))

def tinh_chuyen_vi(matran):
    return list(map(list, zip(*matran)))

def kiem_tra_doi_xung(matran):
    chuyen_vi = tinh_chuyen_vi(matran)
    return matran == chuyen_vi
