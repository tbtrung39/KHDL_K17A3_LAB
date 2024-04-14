password = input("Nhập mật khẩu: ")

if len(password) < 6 or len(password) > 12:
    print("Mật khẩu không hợp lệ!")
else:
    ki_tu_chu = False
    ki_tu_so = False
    ki_tu_dac_biet = False

    for char in password:
        if char.isalpha():
            ki_tu_chu = True
        elif char.isdigit():
            ki_tu_so = True
        elif char in "$#@":
            ki_tu_dac_biet = True

    if ki_tu_chu and ki_tu_so and ki_tu_dac_biet:
        print("Mật khẩu hợp lệ!")
    else:
        print("Mật khẩu không hợp lệ!")
