def tao_tu_dien(n):
    tu_dien = {}
    for i in range(1, n + 1):
        tu_dien[i] = i * i
    return tu_dien

n = int(input("Nhập số nguyên dương n: "))
ket_qua = tao_tu_dien(n)
print("Từ điển được tạo ra là:", ket_qua)
