def nhap_ma_tran(n):
    return [list(map(int, input().split())) for _ in range(n)]
def in_ma_tran(ma_tran):
    for hang in ma_tran:
        print(" ".join(map(str, hang)))
def chuyen_vi(ma_tran):
    return list(map(list, zip(*ma_tran)))
def kiem_tra_doi_xung(ma_tran):
    return ma_tran==chuyen_vi(ma_tran)