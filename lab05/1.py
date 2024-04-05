# Nhập chuỗi từ bàn phím
str = input("Nhập chuỗi: ")

# Đếm số kí tự là số trong chuỗi
count = 0
for c in str:
    if c.isdigit():
        count += 1

# In kết quả ra màn hình
print("Số các kí tự là số trong chuỗi là:", count)