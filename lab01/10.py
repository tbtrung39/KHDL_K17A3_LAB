a = float(input("Nhập vận tốc hiện tại của ô tô (m/s): "))
if a < 0:
    print("Vận tốc không thể là số âm.")
else:
    t = 0
    v = a ** 4
    while v > 0:
        v = -t * 1.16 + a ** 4
        if v < 0:
            break
        t += 0.01  # Tăng thời gian theo bước 0.01 để gần đúng kết quả
    time = "{:.2f}".format(t)
    print("Thời gian ô tô dừng lại khi người lái đạp phanh là:", time, "giây.")
