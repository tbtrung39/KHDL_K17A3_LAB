import quanlysinhvien


data = [
    ['Tên SV','Điểm rèn luyện','Điểm trung bình'],
    ['A',78,7.6],
    ['B',90,8.7],
    ['C',82,9.3]
]

filename = 'ds_sinhvien.csv'

with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
    for row in data:
        row_str = ','.join(str(field) for field in row)
        csvfile.write(row_str + '\n')

def main():
    import quanlysinhvien
    dtb = float(input("Nhập điểm trung bình sinh viên: "))
    drl = int(input('Nhập điểm rèn luyện của sinh viên: '))
    print(quanlysinhvien.tinh_diem_tich_luy(dtb,drl))

    list = []
    list.append(quanlysinhvien.tinh_diem_tich_luy(dtb,drl))
    new_list = list.sort(drl,reverse=False)
    print(new_list)


         

    # Lưu danh sách nhân viên vào file CSV
import os
import csv

    # Lưu danh sách nhân viên vào file CSV
folder_path = "files"  # Đường dẫn đến folder chứa file CSV
file_path = os.path.join(folder_path, "D:\Thực tập lập trình cơ bản\lab11_TTLT\My_QuanLySinhvien\quanlysinhvien.py")  # Đường dẫn đầy đủ của file CSV

with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["Tên SV","ĐRL","ĐTB"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
if __name__ == "__main__":
    main()
                