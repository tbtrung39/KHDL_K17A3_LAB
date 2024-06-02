import re

password = input('nhập mật khẩu')

if 6 <= len(password) <= 12:
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"\d", password) and re.search(r"%@#", password):
        print("Mật khẩu hợp lệ!")
    else:
        print("Mật khẩu không hợp lệ!")
else:
    print("Mật khẩu không hợp lệ!")