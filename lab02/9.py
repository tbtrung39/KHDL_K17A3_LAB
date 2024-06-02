so_kwh = int(input("Nhập số kwh: "))
if so_kwh <0:
    print("Số kwh không hợp lệ, vui lòng nhập lại")
else:
    if so_kwh >= 0 and so_kwh <=100:
        don_gia = so_kwh * 2000
    elif so_kwh >100 and so_kwh <=200:
        don_gia = (100 * 2000) + ((so_kwh -100) * 2500)
    elif so_kwh > 200 and so_kwh <=300:
        don_gia = (100 * 2000) + (100 * 2500) + ((so_kwh - 200) * 3000)
    else:
        don_gia = (100 * 2000) + (100 * 2500) + (100 * 3000) + ((so_kwh - 300) * 5000)
    print("Tiền điện phải trả là: ",don_gia)                 