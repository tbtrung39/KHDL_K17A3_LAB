mat_khau = input("Nhập mật khẩu: ")
danh_sach_mat_khau = mat_khau.split(",")

ky_tu_dac_biet = ['$', '#', '@', '+']
mat_khau_hop_le = []

for mat_khau in danh_sach_mat_khau:
    if len(mat_khau) < 6 or len(mat_khau) > 12:
        print("Mật khẩu",mat_khau,"không hợp lệ vì độ dài không nằm trong khoảng 6-12 ký tự.")
        continue
    
    co_chu_thuong = False
    co_chu_hoa = False
    co_so = False
    co_ky_tu_dac_biet = False
    
    for ky_tu in mat_khau:
        if ky_tu.islower():
            co_chu_thuong = True
        elif ky_tu.isupper():
            co_chu_hoa = True
        elif ky_tu.isdigit():
            co_so = True
        elif ky_tu in ky_tu_dac_biet:
            co_ky_tu_dac_biet = True
    
    if not (co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet):
        print(f"Mật khẩu '{mat_khau}' không hợp lệ vì không chứa đủ các loại ký tự (chữ thường, chữ hoa, số, ký tự đặc biệt).")
        continue
    
    mat_khau_hop_le.append(mat_khau)

if mat_khau_hop_le:
    print("mật khẩu hợp lệ")
    for mat_khau in mat_khau_hop_le:
        print(mat_khau)
else:
    print("mật khẩu không hợp lệ.")