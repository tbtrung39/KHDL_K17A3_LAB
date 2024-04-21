# Nhập số phần tử vào danh sách
n = int(input("Nhập số phần tử của danh sách: "))
danhsach = []
for i in range(n):
    x = int(input("Nhập phần tử thứ {}:".format(i+1)))
    danhsach.append(x)

# Tìm phần tử lớn thứ hai và vị trí của phần tử đạt giá trị lớn thứ hai
sorted_danhsach = sorted(danhsach, reverse=True)
second_largest = sorted_danhsach[1]
second_largest_index = danhsach.index(second_largest)
print("Phần tử lớn thứ hai:", second_largest)
print("Vị trí của phần tử lớn thứ hai:", second_largest_index)

# Tính số lượng các số dương liên tiếp nhiều nhất
tong_so_duong_lien_tiep = 0
current_consecutive_positive = 0
for x in danhsach:
    if x > 0:
        current_consecutive_positive += 1
        tong_so_duong_lien_tiep = max(tong_so_duong_lien_tiep, current_consecutive_positive)
    else:
        current_consecutive_positive = 0
print("Số lượng các số dương liên tiếp nhiều nhất:", tong_so_duong_lien_tiep)

tong_so_duong_lien_tiep = 0
current_sum_consecutive_positive = 0
for x in danhsach:
    if x > 0:
        current_sum_consecutive_positive += x
        tong_so_duong_lien_tiep = max(tong_so_duong_lien_tiep, current_sum_consecutive_positive)
    else:
        current_sum_consecutive_positive = 0
print("Tổng lớn nhất của các số dương liên tiếp:", tong_so_duong_lien_tiep)
