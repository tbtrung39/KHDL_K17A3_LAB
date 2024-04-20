dictionary = {}
n = int(input('Nhập số lượng nhân viên: '))

for i in range(n):
    ma_nv = input('Nhập mã nhân viên (4 ký tự số): ')
    ho_ten = input('Nhập họ và tên nhân viên (tối đa 20 ký tự): ')
    nam_sinh = int(input('Nhập năm sinh của nhân viên: '))
    luong = float(input('Nhập lương của nhân viên: '))
    dictionary[ma_nv] = {'Họ và tên': ho_ten, 'Năm sinh': nam_sinh, 'Lương': luong}

ma_nv_tim_kiem = input('Nhập mã nhân viên cần tìm kiếm: ')
if ma_nv_tim_kiem in dictionary:
    print('Thông tin nhân viên:')
    print(f'Mã nhân viên: {ma_nv_tim_kiem}')
    for key, value in dictionary[ma_nv_tim_kiem].items():
        print(f'{key}: {value}')
else:
    print('Không tìm thấy nhân viên có mã số này.')

ma_nv_tang_luong = input('Nhập mã nhân viên cần tăng lương: ')
muc_tang = float(input('Nhập số tiền muốn tăng lương: '))
if ma_nv_tang_luong in dictionary:
    dictionary[ma_nv_tang_luong]['Lương'] += muc_tang
    print(f'Đã tăng lương cho nhân viên có mã {ma_nv_tang_luong}.')
else:
    print('Không tìm thấy nhân viên có mã số này')

ma_nv_xoa = input('Nhập mã nhân viên cần xóa: ')
if ma_nv_xoa in dictionary:
    del dictionary[ma_nv_xoa]
    print(f'Đã xóa nhân viên có mã {ma_nv_xoa} khỏi danh sách.')
else:
    print('Không tìm thấy nhân viên có mã số này.')

dictionary_sap_xep = dict(sorted(dictionary.items(), key=lambda x: x[1]['Năm sinh'], reverse=True))
print('\nDanh sách nhân viên sau khi sắp xếp giảm dần theo năm sinh:')
for ma_nv, thong_tin in dictionary_sap_xep.items():
    print(f'Mã nhân viên: {ma_nv}, Họ và tên: {thong_tin['Họ và tên']}, Năm sinh: {thong_tin['Năm sinh']}, Lương: {thong_tin['Lương']}')
