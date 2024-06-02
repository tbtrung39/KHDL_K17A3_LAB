def nhap_ma_tran():
    N = int(input("Nhập kích thước ma trận N: "))
    ma_tran = []
    for i in range(N):
        hang = list(map(int, input(f"Nhập hàng thứ {i+1} (N số nguyên cách nhau bằng khoảng trắng): ").split()))
        if len(hang) != N:
            print(f"Vui lòng nhập đúng {N} số nguyên cho mỗi hàng.")
            return nhap_ma_tran()
        ma_tran.append(hang)
    return ma_tran
def in_ma_tran(ma_tran):
    for hang in ma_tran:
        print(" ".join(map(str, hang)))
def tinh_chuyen_vi(ma_tran):
    N = len(ma_tran)
    chuyen_vi = [[ma_tran[j][i] for j in range(N)] for i in range(N)]
    return chuyen_vi
def kiem_tra_doi_xung(ma_tran):
    N = len(ma_tran)
    for i in range(N):
        for j in range(N):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True
