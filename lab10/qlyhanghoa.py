# qlyhanghoa.py

def nhap_thong_tin_hang_hoa():
    danh_sach_hang_hoa = []
    so_luong_hang_hoa = int(input("Nhập số lượng mặt hàng: "))
    
    for i in range(so_luong_hang_hoa):
        ma_hang = input("Nhập mã hàng (4 kí tự): ")
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = int(input("Nhập số lượng: "))
        
        thanh_tien = don_gia * so_luong
        thue = thanh_tien * 0.1
        
        danh_sach_hang_hoa.append({
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "don_vi_tinh": don_vi_tinh,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": thanh_tien,
            "thue": thue
        })
    
    return danh_sach_hang_hoa

def sap_xep_theo_thue(danh_sach_hang_hoa):
    return sorted(danh_sach_hang_hoa, key=lambda x: x["thue"], reverse=True)

if __name__ == "__main__":
    danh_sach_hang_hoa = nhap_thong_tin_hang_hoa()
    print("\nDanh sách hàng hóa trước khi sắp xếp:")
    for hang_hoa in danh_sach_hang_hoa:
        print(hang_hoa)
    
    danh_sach_sau_sap_xep = sap_xep_theo_thue(danh_sach_hang_hoa)
    print("\nDanh sách hàng hóa sau khi sắp xếp:")
    for hang_hoa in danh_sach_sau_sap_xep:
        print(hang_hoa)
