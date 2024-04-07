bin_str = input("Nhập chuỗi số nhị phân: ")
dec_str = 0
for num in bin_str:
    dec_str = dec_str * 2 + int(num)
print("Chuỗi số thập phân đã chuyển đổi là: ", dec_str)