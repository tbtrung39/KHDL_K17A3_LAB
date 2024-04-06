chuỗi_nhị_phân = input("Nhập chuỗi nhị phân: ")

while not set(chuỗi_nhị_phân) <= {"0", "1"}:
    print("Đây không phải là chuỗi nhị phân. Vui lòng nhập lại.")
    chuỗi_nhị_phân = input("Nhập chuỗi nhị phân: ")

số_thập_phân = int(chuỗi_nhị_phân, 2)
print("Số thập phân tương ứng là:", số_thập_phân)
