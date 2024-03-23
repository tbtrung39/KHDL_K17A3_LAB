
a = float(input("Nhập vận tốc ban đầu của ô tô (km/h): "))
t = (a**4) / (1.3219280948873626 - a)
thoi_gian_dung = round(t, 2)
print(f"Thời gian ô tô đi được cho đến lúc dừng là: {thoi_gian_dung} giây")
