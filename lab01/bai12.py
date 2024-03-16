import math
v = float(input("Nhập vận tốc: "))
t = v**4 / math.log(5,4)
print(f"Thời gian xe đi được từ lúc đạp phanh tới lúc dừng là: {round(t,2)}")