# Nhập chuỗi nhị phân từ người dùng
chuoi_nhi_phan = input("Nhập chuỗi nhị phân: ")

thap_phan = 0
mu = len(chuoi_nhi_phan) - 1
for chu_so in chuoi_nhi_phan:
    if chu_so == '1':
        thap_phan += 2 ** mu
    mu -= 1
print("Số thập phân tương ứng là:", thap_phan)
