data = [
    ['Tên NV','Chức Vụ','Thực Lĩnh']
    ['A','TP',76000000]
    ['B','PP',65000000]
    ['C','NV',15000000]
]

filename = 'ds_nhanvien.csv'
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    for row in data:
        row_str = ','.join(str(field) for field in row)
        csvfile.write(row_str + '\n')

def main():
    danh_sach_nhan_vien = []
    n = int(input("Nhập số lượng nhân viên là : "))
    for i in range(n):
        ten_nv = input(f"Nhập tên nhân viên thứ {i+1}: ")
        he_so = float(input(f"Nhập hệ số nhân viên thứ {i+1}: "))
        chuc_vu = input(f"Chức vụ của nhân viên thứ {i+1}: ")
        luong = he_so*1490000
        if chuc_vu == "TP" :
            phu_cap = 1000000
        elif chuc_vu == "PP":
            phu_cap = 700000
        elif chuc_vu == "NV":
            phu_cap = 300000
        thuc_linh = luong + phu_cap






        nhan_vien = {
            "Tên": ten_nv,
            "Hệ số": he_so,
            "Chức Vụ": chuc_vu,
            "Thực Lĩnh": thuc_linh
        }


        danh_sach_nhan_vien.append(nhan_vien)
        print(danh_sach_nhan_vien)


    # Lưu danh sách nhân viên vào file csv
import os
import csv
folder_path = "files"       #Đường dẫn đến folder chứa file csv
file_path = os.path.join(folder_path,"" )

with open(file_path, mode="w", newline="", encoding="utf-8") as file:
    filename = ["Tên NV", "Chức Vụ", "Thực Lĩnh"]
    writer = csv.DictWriter(file, filenames=filename)
if __name__ == "__main__":
    main()