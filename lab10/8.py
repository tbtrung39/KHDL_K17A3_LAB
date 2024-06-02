import Matranvuong
def main():
    ma_tran = Matranvuong.nhap_ma_tran()
    print("Ma trận đã nhập:")
    Matranvuong.in_ma_tran(ma_tran)
    chuyen_vi = Matranvuong.tinh_chuyen_vi(ma_tran)
    print("\nMa trận chuyển vị:")
    Matranvuong.in_ma_tran(chuyen_vi)
    doi_xung = Matranvuong.kiem_tra_doi_xung(ma_tran)
    if doi_xung:
        print("\nMa trận này là ma trận đối xứng.")
    else:
        print("\nMa trận này không phải là ma trận đối xứng.")
if __name__ == "__main__":
    main()
