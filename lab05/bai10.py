chuoi = input("Nhập chuỗi nhị phân: ")
count = 0
for digit in chuoi:
    count = count * 2 + int(digit)
print("Số thập phân tương ứng của chuỗi nhị phân", chuoi, "là:", count)
