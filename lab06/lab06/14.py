password = input("Nhập mật khẩu: ")
ds_password = password.split(",")

ky_tu_dac_biet = ['$', '#', '@', '+']
password_hop_le = []

for password in ds_password:
    if len(password) < 6 or len(password) > 12:
        print(f"Mật khẩu '{password}' không hợp lệ vì độ dài không nằm trong khoảng 6-12 ký tự.")
        continue

    co_chu_thuong = False
    co_chu_hoa = False
    co_so = False
    co_ky_tu_dac_biet = False

    for ky_tu in password:
        if ky_tu.islower():
            co_chu_thuong = True
        elif ky_tu.isupper():
            co_chu_hoa = True
        elif ky_tu.isdigit():
            co_so = True
        elif ky_tu in ky_tu_dac_biet:
            co_ky_tu_dac_biet = True

    if not (co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet):
        print(f"Mật khẩu '{password}' không hợp lệ vì không chứa đủ các loại ký tự (chữ thường, chữ hoa, số, ký tự đặc biệt).")
        continue

    password_hop_le.append(password)

if password_hop_le:
    print("mật khẩu hợp lệ")
    for password in password_hop_le:
        print(password)
else:
    print("mật khẩu không hợp lệ.")