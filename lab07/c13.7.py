n = input("Nhập chuỗi ký tự n: ")
tu_dien = {}
for i in range(len(n)):
    for j in range(i + 1, len(n) + 1):
        sub_str = n[i:j]
        count = n.count(sub_str)
        if sub_str not in tu_dien:
            tu_dien[sub_str] = count
print(tu_dien)