import os
import csv

def tinh_diem_tich_luy(dtb, drl):
    return dtb + drl / 10

def main():
    data = [
        ['Tên SV', 'Điểm rèn luyện', 'Điểm trung bình'],
        ['A', 78, 7.6],
        ['B', 90, 8.7],
        ['C', 82, 9.3]
    ]
    filename = 'ds_sinhvien.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)
    dtb = float(input("Nhập điểm trung bình sinh viên: "))
    drl = int(input('Nhập điểm rèn luyện của sinh viên: '))
    cum_score = tinh_diem_tich_luy(dtb, drl)
    print(f"Điểm tích lũy của sinh viên là: {cum_score}")
if __name__ == "__main__":
    main()

                