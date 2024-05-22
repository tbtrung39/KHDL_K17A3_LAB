def them_thong_tin():
    ma_hang = input("Nhập mã hàng: ")
    ten_hang = input("Nhập tên hàng: ")
    don_vi_tinh = input("Nhập đơn vị tính: ")
    don_gia = float(input("Nhập đơn giá: "))
    while don_gia <=0:
        don_gia = float(input("Đơn giá không hợp lệ, hãy nhập lại: "))
    so_luong = int(input("Nhập số lượng: "))
    while so_luong <=0:
        so_luong = int(input("Nhập số lượng: "))
    thanh_tien = don_gia * so_luong    
    thue = thanh_tien * 0.1
    #return {"Mã hàng hóa": ma_hang, "Tên hàng hóa": ten_hang, "Đơn vị tính": don_vi_tinh, "Đơn giá": don_gia, "Số lượng": so_luong, "Thành tiền": thanh_tien, "Thuế VAT": thue}
    HangHoa = {
        "Mã hàng hóa": ma_hang,
        "Tên hàng hóa": ten_hang,
        "Đơn vị tính": don_vi_tinh,
        "Đơn giá": don_gia,
        "Số lượng": so_luong,
        "Thành tiền": thanh_tien,
        "Thuế VAT": thue
        
    }
    return HangHoa
def tinh_thue(HangHoa):
    return HangHoa["Thuế VAT"]

def sap_xep(danh_sach_hang_hoa):
    return sorted(danh_sach_hang_hoa, key = tinh_thue, reverse= True)

def in_danh_sach(danh_sach_hang_hoa):
    print("{:<10} {:<40} {:<30} {:<25}".format("Mã hàng hóa","Tên hàng hóa","Thành tiền","Thuế VAT"))
    for hang_hoa in danh_sach_hang_hoa:
        print("{:<10} {:<40} {:<30} {:<25}".format(hang_hoa["Mã hàng hóa"],hang_hoa["Tên hàng hóa"],hang_hoa["Thành tiền"],hang_hoa["Thuế VAT"]))