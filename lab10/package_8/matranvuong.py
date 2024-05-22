def tao_ma_tran(n):
    ma_tran = []
    for i in range(n):
        row = []
        for j in range(n):
            phan_tu = int(input(f"Nhập phần tử [{i}][{j}]: "))
            row.append(phan_tu)
        ma_tran.append(row)
    return ma_tran

def in_ma_tran(ma_tran):
    for row in ma_tran:
        print(" ".join(map(str, row)))

def chuyen_vi_ma_tran(ma_tran):
    n = len(ma_tran)
    ma_tran_chuyen_vi = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(ma_tran[j][i])
        ma_tran_chuyen_vi.append(row)
    return ma_tran_chuyen_vi

def in_ma_tran_chuyen_vi(ma_tran_chuyen_vi):
    for row in ma_tran_chuyen_vi:
        print(" ".join(map(str, row)))

    