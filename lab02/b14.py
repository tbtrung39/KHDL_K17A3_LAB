import math

I_0 = float(input("Nhập mức cường độ âm gốc tại nguồn phát (dB): "))
D = float(input("Nhập khoảng cách từ người nghe đến nguồn phát (m): "))
D_0 = 1  # Khoảng cách tham chiếu (m)
L = 20 * math.log10(D / D_0)
I = I_0 - L

if I > 100:
    print("Người nghe có thể nghe thấy âm.")
else:
    print("Người nghe không thể nghe thấy âm.")