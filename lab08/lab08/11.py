def tinh_diem_tb(toan, ly, hoa):
    diem_tb = (toan + ly + hoa)/3
    return diem_tb

ho_va_ten = input('Nhập họ và tên sinh viên: ')

toan = float(input('Nhập điểm môn Toán: '))
ly = float(input('Nhập điểm môn Lý: '))
hoa = float(input('Nhập điểm môn Hóa: '))

diem_tb = tinh_diem_tb(toan,ly,hoa)
print(f'Họ và tên: {ho_va_ten}')
print(f'Điểm trung bình là: {diem_tb}')