import os
import csv


data = [
    ['Tên NV', 'Chức vụ', 'Thực lĩnh'],
    ['A', 'TP', 76000000],
    ['B', 'PP', 65000000],
    ['C', 'NV', 15000000]
]

filename = 'ds_nhanvien.csv'


with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

def main():
    danh_sach_nhan_vien = []
    n = int(input("Nhập số lượng nhân viên: "))
    
    for i in range(n):
        ten_nv = input(f"Nhập tên nhân viên thứ {i+1}: ")
        he_so = float(input(f"Nhập hệ số nhân viên thứ {i+1}: "))
        chuc_vu = input(f"Chức vụ nhân viên thứ {i+1} là: ")
        luong = he_so * 1490000

        if chuc_vu == 'TP':
            phu_cap = 1000000
        elif chuc_vu == 'PP':
            phu_cap = 700000
        elif chuc_vu == 'NV':
            phu_cap = 300000
        else:
            phu_cap = 0 
        
        thuc_linh = luong + phu_cap
        
        nhan_vien = {
            "Tên NV": ten_nv,
            "Chức vụ": chuc_vu,
            "Thực lĩnh": thuc_linh
        }
        
        danh_sach_nhan_vien.append(nhan_vien)
    
    print(danh_sach_nhan_vien)


    folder_path = "files"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

   
    file_path = os.path.join(folder_path, filename)
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ["Tên NV", "Chức vụ", "Thực lĩnh"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        
        if file.tell() == 0:
            writer.writeheader()
        
  
        for nhan_vien in danh_sach_nhan_vien:
            writer.writerow(nhan_vien)

if __name__ == "__main__":
    main()
