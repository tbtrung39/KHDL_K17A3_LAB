def nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False
    
def so_ngay_toi_da_trong_thang(m, y):
    if m in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif m in {4, 6, 9, 11}:
        return 30
    elif m == 2:
        if nam_nhuan(y):
            return 29
        else:
            return 28
    else:
        return None

nam = int(input('Nhập một năm: '))
if nam_nhuan(nam):
    print(f'{nam} là năm nhuận.')
else:
    print(f'{nam} không phải là năm nhuận.')

m = int(input('Nhập tháng (1-12): '))
y = int(input('Nhập năm: '))

so_ngay = so_ngay_toi_da_trong_thang(m, y)

if so_ngay is not None:
    print(f'Số ngày tối đa của tháng {m} năm {y} là: {so_ngay}')
else:
    print('Tháng không hợp lệ.')
