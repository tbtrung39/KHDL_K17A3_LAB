I = float(input("Nhập mức cường độ âm thanh I (dB): "))
D = float(input("Nhập khoảng cách từ nguồn âm đến người nghe D (m): "))
muc_cuong_do_am_thanh_I = 10**(I / 10)
if muc_cuong_do_am_thanh_I >= 10**(100 / 10):
    print("Người đó nghe thấy âm.")
else:
    print("Người đó không nghe thấy âm")