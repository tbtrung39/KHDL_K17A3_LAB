import package_7

day_so_ngau_nhien = package_7.ds.tao_day_so()
print("Dãy số đã tạo là:")
print(day_so_ngau_nhien)

day_so_chia_7 = package_7.ds.day_so_nguyen_to_chia_7(day_so_ngau_nhien)
if day_so_chia_7:
    print("Dãy số nguyên tố chia hết cho 7 từ dãy số đã tạo là:")
    print(day_so_chia_7)
else:
    print("Dãy số đã tạo không có số nguyên tố chia hết cho 7")

day_so_chinh_phuong = package_7.ds.day_so_chinh_phuong(day_so_ngau_nhien)
if day_so_chinh_phuong:
    print("Dãy số chính phương từ dãy số đã tạo là:")
    print(day_so_chinh_phuong)
else:
    print("Dãy số đã tạo không có số chính phương")      