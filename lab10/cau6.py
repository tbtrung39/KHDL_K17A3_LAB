import package1.doicoso2 as t 

ky_tu = "123ABCXYZ"
print("Chuỗi ký tự sau khi loại bỏ: ",t.loai_bo_ky_tu(ky_tu))  

chuoi_so = "1010"
print(f"{chuoi_so} thuộc cơ số {t.co_so_chuoi_so(chuoi_so)}")  
print(f"Cơ số 2 sang cơ số 10: {chuoi_so} --> {t.chuyen_doi_co_so(chuoi_so,2)}")

chuoi_so_bat_phan = "1311"
print(f"Cơ số 8 sang cơ số 10: {chuoi_so_bat_phan} --> {t.chuyen_doi_co_so(chuoi_so_bat_phan,8)}") 

chuoi_so_thap_luc_phan = "888BCD"
print(f"Cơ số 16 sang cơ số 10 :{chuoi_so_thap_luc_phan} --> {t.chuyen_doi_co_so(chuoi_so_thap_luc_phan,16)}")