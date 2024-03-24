# CT đã cho: v(t) = -t * log(5) + a^4
import math
V_ban_dau = float(input("Nhập vận tốc ban đầu của xe ô tô: "))
a = float(input("Nhập giá trị của a: "))

t = (a**4 + V_ban_dau) / math.log(5, 4)

print(f"Xe ô tô sẽ dừng lại sau khoảng {t} giây")