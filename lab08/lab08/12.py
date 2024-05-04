def tinh_luong(tham_nien):
    # Giả sử mỗi năm thâm niên tương ứng với mức lương tăng 15%
    muc_luong_co_ban = 1000000  # Giả sử mức lương cơ bản là 1.000.000 VND
    ty_le_tang_luong = 0.15  # Tỷ lệ tăng lương mỗi năm thâm niên

    luong = muc_luong_co_ban * (1 + ty_le_tang_luong * tham_nien)

    return luong

def nhap_thong_tin_nhan_vien():
    ho_ten = input('Nhập họ và tên của nhân viên: ')
    que_quan = input('Nhập quê quán của nhân viên: ')
    tham_nien = int(input('Nhập số năm thâm niên công tác của nhân viên: '))
    return ho_ten, que_quan, tham_nien

while True:
    ho_ten, que_quan, tham_nien = nhap_thong_tin_nhan_vien()

    luong = tinh_luong(tham_nien)

    print(f'Họ và tên nhân viên: {ho_ten}')
    print(f'Quê quán: {que_quan}')
    print(f'Thâm niên công tác: {tham_nien} năm')
    print(f'Lương của nhân viên là: {luong} VND')

    tiep_tuc = input('Bạn có muốn nhập thông tin cho nhân viên khác không? (C/K): ')
    if tiep_tuc.upper() != 'C':
        break
