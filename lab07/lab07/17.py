sv = {}
n = int(input('Nhập số lượng sinh viên: '))
count = 0

while count < n:
    ma_sv = input(f'Nhập mã sinh viên của sinh viên thứ {count + 1}: ')
    ten_sv = input(f'Nhập tên sinh viên của sinh viên thứ {count + 1}: ')
    while True:
        diem_sv = int(input(f'Nhập điểm số của sinh viên thứ {count + 1} (0-10): '))
        if diem_sv in range(11):
            break
        else:
            print('Điểm số phải thuộc khoảng từ 0 đến 10.')
    sv[ma_sv] = {'Tên': ten_sv, 'Điểm': diem_sv}
    count += 1

sv_sap_xep = sorted(sv.items(), key=lambda x: x[1]['Điểm'], reverse=True)
print('\nDanh sách sinh viên theo điểm số giảm dần:')
for ma_sv, info in sv_sap_xep:
    print(f"Mã sinh viên: {ma_sv}, Tên sinh viên: {info['Tên']}, Điểm số: {info['Điểm']}")
