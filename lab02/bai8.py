tnct = int(input("Nhập thâm niên công tác: "))
luong_cb = 1350000
if tnct < 12:
    luong = 2.34 * luong_cb
elif 12 <= tnct < 36:
    luong = 3.33 * luong_cb
elif 36 <= tnct < 60:
    luong = 3.66 * luong_cb
else:
    luong = 3.99 * luong_cb
print("Tiền lương: ", luong)