import math
S = float(input("Nhập mức cường độ âm của nguồn âm (dB): "))
D = float(input("Nhập khoảng cách từ nguồn âm đến người nghe (m): "))
I = S - 20 * math.log10(D)
if I >= 100:
    print("Người này sẽ nghe thấy âm.")
else:
    print("Người này sẽ không nghe thấy âm.")