import math

a = float(input("Nhập vận tốc ban đầu của xe ô tô (m/s): "))
t = -1 * math.log(a, 5) / math.log(5, 4)
print("Thời gian để ô tô dừng lại là:", round(t, 2), "giây")