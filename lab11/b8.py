import csv
import os
danh_sach = [
    ['Tên NV', 'Chức Vụ', 'Thực Lĩnh'],
    ['A', 'TP', 76000000],
    ['B', 'PP', 65000000],
    ['C', 'NV', 15000000]
]

filename = 'ds_nhanvien.csv'
folder_path = "files"
file_path = os.path.join(folder_path, filename)
os.makedirs(folder_path, exist_ok=True)
with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(danh_sach)
def main():
    danh_sach_nhan_vien = []
    while True:
        ten_nv = input("Nhập tên nhân viên (hoặc 'exit' để dừng): ")
        if ten_nv.lower() == 'exit':
            break
        try:
            he_so = float(input(f"Nhập hệ số của {ten_nv}: "))
        except ValueError:
            print("Hệ số phải là một số. Vui lòng thử lại.")
            continue
        
        chuc_vu = input(f"Chức vụ của {ten_nv} (TP/PP/NV): ")
        luong = he_so * 1490000
        
        if chuc_vu == "TP":
            phu_cap = 1000000
        elif chuc_vu == "PP":
            phu_cap = 700000
        elif chuc_vu == "NV":
            phu_cap = 300000
        else:
            print("Chức vụ không hợp lệ. Vui lòng thử lại.")
            continue
        
        thuc_linh = luong + phu_cap

        nhan_vien = {
            "Tên NV": ten_nv,
            "Chức Vụ": chuc_vu,
            "Thực Lĩnh": thuc_linh
        }

        danh_sach_nhan_vien.append(nhan_vien)
        print("Danh sách nhân viên hiện tại:", danh_sach_nhan_vien)
    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["Tên NV", "Chức Vụ", "Thực Lĩnh"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if os.stat(file_path).st_size == 0:
            writer.writeheader()
        for nv in danh_sach_nhan_vien:
            writer.writerow(nv)

if __name__ == "__main__":
    main()

