import os
import csv
import quanlysinhvien

# Data to be written to CSV
data = [
    ['Tên SV', 'Điểm rèn luyện', 'Điểm trung bình'],
    ['A', 78, 7.6],
    ['B', 90, 8.7],
    ['C', 82, 9.3]
]

filename = 'ds_sinhvien.csv'

# Ensure the folder exists
folder_path = "files"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_path = os.path.join(folder_path, filename)

# Write data to CSV file
with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

def main():
    dtb = float(input("Nhập điểm trung bình sinh viên: "))
    drl = int(input('Nhập điểm rèn luyện của sinh viên: '))
    tich_luy = quanlysinhvien.tinh_diem_tich_luy(dtb, drl)
    print("Điểm tích lũy:", tich_luy)

    # Create a list and sort it
    score_list = [{'ĐRL': drl, 'ĐTB': dtb, 'Điểm tích lũy': tich_luy}]
    score_list.sort(key=lambda x: x['ĐRL'])

    print("Sorted list based on ĐRL:", score_list)

    # Write sorted list to another CSV file
    output_filename = 'sorted_sinhvien.csv'
    output_file_path = os.path.join(folder_path, output_filename)

    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['ĐRL', 'ĐTB', 'Điểm tích lũy']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(score_list)

if __name__ == "__main__":
    main()
