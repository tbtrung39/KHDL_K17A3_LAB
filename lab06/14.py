while True:
    password = input("Nhập mật khẩu mới: ")
    if len(password) < 6 or len(password) > 12:
        print("do dai mat khau phai tu 6-12")
    elif not any(c.islower() for c in password):
        print("mat khau phai co it nhat 1 chu trong (a-z).")
    elif not any(c.isupper() for c in password):
        print("mat khau phai co it nhat 1 chu trong (A-Z).")
    elif not any(c.isdigit() for c in password):
        print("mat khau phai co it nhat 1 chu so trong (0-9).")
    elif not any(c in "$#@ " for c in password):
        print("mat khau phai co it nhat 1 ky tu trong ($#@).")
    else:
        print("mat khau hop le!!!")
        break