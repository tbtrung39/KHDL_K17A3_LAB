from package import qlyhanghoa as md
items = []
thanh_tien = 0
thue_vat = 0

while True:
    ma_hang = input("Nhập mã hàng: ")
    if ma_hang == 'esc':
        break
    
    ten_hang = input("Nhập tên hàng: ")
    if ten_hang.isdigit():
        print("Tên hàng không hợp lệ!")
        continue
    
    don_vi = input("Đơn vị tính tiền: ")
    if don_vi.isdigit():
        print("Đơn vị tính không hợp lệ!")
        continue
    
    don_gia = input("Đơn có giá là: ")
    if not don_gia.isdigit():
        print("Đơn giá phải là số!")
        continue
    don_gia = float(don_gia)
    
    so_luong = input("Nhập số lượng hàng: ")
    if not so_luong.isdigit():
        print("Số lượng phải là số!")
        continue
    so_luong = int(so_luong)
    
    thanh_tien_hang = don_gia * so_luong
    thue_vat_hang = thanh_tien_hang * 0.1

    thanh_tien += thanh_tien_hang
    thue_vat += thue_vat_hang

    item_info = md.qly(ma_hang, ten_hang, don_vi, don_gia, so_luong, thanh_tien_hang, thue_vat_hang)
    items.append(item_info)
    print(f"Thông tin chi tiết hàng hóa: {item_info}")

# Sort items by VAT in descending order
sorted_items = sorted(items, key=lambda x: x[6], reverse=True)

print("Danh sách các mặt hàng sau khi sắp xếp theo thuế VAT giảm dần:")
for item in sorted_items:
    print(item)

print(f"Tổng thành tiền: {thanh_tien}")
print(f"Tổng thuế VAT: {thue_vat}")