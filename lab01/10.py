# Nhập vào vận tốc a
a = float(input("Nhập vào vận tốc a của xe ô tô: "))

# Tính thời gian xe ô tô đi được cho đến lúc dừng
t = 0
while True:
    # Tính logarit cơ số 4 của 5
    log_4_of_5 = 0
    x = 5
    while x > 1:
        x /= 4
        log_4_of_5 += 1

    # Tính vận tốc v
    v = -t * log_4_of_5 + a**4

    # Kiểm tra nếu vận tốc v <= 0 thì dừng lại
    if v <= 0:
        break

    # Tăng thời gian t lên
    t += 0.01

# In ra thời gian t (làm tròn đến 2 chữ số thập phân)
print("Thời gian ô tô đi được cho đến lúc dừng là: {:.2f} giây".format(t))
