def tao_tu_dien(chuoi):
    tu_dien = {}
    for i in range(len(chuoi)):
        for j in range(i + 1, len(chuoi) + 1):
            k = chuoi[i:j]
            if k in tu_dien:
                tu_dien[k] += 1
            else:
                tu_dien[k] = 1
    return tu_dien

chuoi = input("Nhập chuỗi ký tự: ")
tu_dien = tao_tu_dien(chuoi)

print("Từ điển được tạo ra là:", tu_dien)
