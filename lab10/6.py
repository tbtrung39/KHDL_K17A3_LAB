import doicoso2
def main():
    chuoi = doicoso2.nhap_chuoi()
    chuoi_sau_khi_loai = doicoso2.loai_bo_ky_tu(chuoi)
    doicoso2.hien_thi_ket_qua(chuoi_sau_khi_loai)
if __name__ == "__main__":
    main()
