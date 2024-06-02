import os
import csv
import quanlysinhvien

data = [
    ['Tên SV', 'Điểm rèn luyện', 'Điểm trung bình'],
    ['A', 78, 7.6],
    ['B', 90, 8.7],
    ['C', 82, 9.3]
]

filename = 'files/ds_sinhvien.csv'

# Write data to CSV
with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

def main():
    dtb = float(input("Nhập điểm trung bình sinh viên: "))
    drl = int(input('Nhập điểm rèn luyện của sinh viên: '))
    
    # Use functions from the quanlysinhvien module
    diem_tich_luy = quanlysinhvien.tinh_diem_tich_luy(dtb, drl)
    print("Điểm tích lũy của sinh viên là:", diem_tich_luy)

    # Using sorted function to sort the list
    list_of_points = [quanlysinhvien.tinh_diem_tich_luy(dtb, drl)]
    sorted_list = sorted(list_of_points, reverse=True)
    print("Danh sách điểm tích lũy đã sắp xếp:", sorted_list)

# File path for saving information
file_path = 'files/quanlysinhvien.csv'

# Write information to CSV
with open(file_path, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["Tên SV", "ĐRL", "ĐTB"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

if __name__ == "__main__":
    main()
