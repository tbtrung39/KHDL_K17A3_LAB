import doiCoso2
chuoi = input('Nhập vào một chuỗi: ')
chuoi_hop_le = doiCoso2.loc_ky_tu(chuoi)

co_so = doiCoso2.xac_dinh_co_so(chuoi_hop_le)
if co_so == 2:
    print(f'Chuỗi {chuoi_hop_le} trong hệ cơ số 2 tương đương với {doiCoso2.chuyen_doi_nhi_phan_sang_thap_phan(chuoi_hop_le)} trong hệ cơ số 10.')
elif co_so == 8:
    print(f'Chuỗi {chuoi_hop_le} trong hệ cơ số 8 tương đương với {doiCoso2.chuyen_doi_bat_phan_sang_thap_phan(chuoi_hop_le)} trong hệ cơ số 10.')
elif co_so == 16:
    print(f'Chuỗi {chuoi_hop_le} trong hệ cơ số 16 tương đương với {doiCoso2.chuyen_doi_thap_luc_phan_sang_thap_phan(chuoi_hop_le)} trong hệ cơ số 10.')
