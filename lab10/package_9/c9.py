import qlyhanghoa
thanh_tien = 0
thue_vat = 0
while True:
    ma_hang = input("Nhập mã hàng: ")
    if ma_hang == 'esc':
        break
    ten_hang = input("Nhập tên hàng: ")
    if ten_hang.isdigit() == True:
        break
    don_vi = input("Đơn vị tính tiền: ")
    if don_vi.isdigit() == True:
        break
    don_gia = input("Đơn có giá là: ")
    if don_gia.isalpha() == True:
        break
    so_luong = input("Nhập số lượng hàng: ")
    if so_luong.isalpha() == True:
        break
thanh_tien += don_gia * so_luong
thue_vat += thanh_tien * 0.1
print(qlyhanghoa.qly(ma_hang,ten_hang,don_vi,don_gia,so_luong,thanh_tien,thue_vat), "là thông tin chi tiết hàng hóa")

