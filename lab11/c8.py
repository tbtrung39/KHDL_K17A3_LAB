data = [
    ['Tên NV','Chức vụ','Thực lĩnh'],
    ['A','TP',76000000],
    ['B','PP',65000000],
    ['C','NV',15000000]
]

filename = 'ds_nhanvien.csv'

with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
    for row in data:
        row_str = ','.join(str(field) for field in row)
        csvfile.write(row_str + '\n')

def main():
    danh_sach_nhan_vien = []
    n = int(input("Nhập số lượng nhân viên: "))
    for i in range(n):
        ten_nv = input(f"Nhập tên nhân viên thứ {i+1}: ")
        he_so = float(input(f"Nhập hệ số nhân viên thứ {i+1}"))
        chuc_vu = input(f"Chức vụ nhân viên thứ {i+1} là: ")
        luong = he_so * 1490000
        if chuc_vu == 'TP':
             phu_cap = 1000000
        elif chuc_vu == 'PP':
             phu_cap = 700000
        elif chuc_vu == 'NV':
             phu_cap = 300000
        thuc_linh = luong + phu_cap

        



        nhan_vien = {
            "Tên": ten_nv,
            "Hệ số": he_so,
            "Chức vụ": chuc_vu,
            "Thực lĩnh": thuc_linh
        }
            

        danh_sach_nhan_vien.append(nhan_vien)
        print(danh_sach_nhan_vien)
         

    # Lưu danh sách nhân viên vào file CSV
import os
import csv

    # Lưu danh sách nhân viên vào file CSV
folder_path = "files"  # Đường dẫn đến folder chứa file CSV
file_path = os.path.join(folder_path, "D:\Thực tập lập trình cơ bản\lab11_TTLT\libs\ds_nhanvien.csv")  # Đường dẫn đầy đủ của file CSV

with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["Tên NV","Chức vụ","Thực lĩnh"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
if __name__ == "__main__":
    main()
                