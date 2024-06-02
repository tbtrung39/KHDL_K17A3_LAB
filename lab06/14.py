import re

mat_khau = input("Nhập mật khẩu: ")

if (6 <= len(mat_khau) <= 12 and
    re.search("[a-z]", mat_khau) and
    re.search("[0-9]", mat_khau) and
    re.search("[A-Z]", mat_khau) and
    re.search("[$#@]", mat_khau)):
    print("Mật khẩu hợp lệ.")
else:
    print("Mật khẩu không hợp lệ.")
