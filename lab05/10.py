while True:
    chuoi_nhi_phan = input("Nhập chuỗi nhị phân(Chuỗi gồm những số 0 và 1): ")
    if set(chuoi_nhi_phan) <= {"0", "1"}:
        so_thap_phan = 0
        for ky_tu in chuoi_nhi_phan:
            so_thap_phan = so_thap_phan * 2 + int(ky_tu)
        print(so_thap_phan)  # In ra số thập phân tương ứng
        break
    else:
        print("Chuỗi bạn nhập không phải là chuỗi nhị phân hợp lệ. Vui long nhap lai")