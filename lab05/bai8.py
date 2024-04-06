chuoi = input("Nhập chuỗi ký tự: ")
max_len = 0
current_len = 0
ket_qua = ''
i = 0
while i < len(chuoi):
    current_len = 1
    while i + 1 < len(chuoi) and chuoi[i] == chuoi[i + 1]:
        current_len += 1
        i += 1

    if current_len > max_len:
        max_len = current_len
        ket_qua = chuoi[i]
    i += 1
chuoi_con_dai_nhat = ket_qua * max_len
print(f"Chuỗi ký tự con có độ dài cực đại và bao gồm các phần tử giống nhau: {chuoi_con_dai_nhat}")