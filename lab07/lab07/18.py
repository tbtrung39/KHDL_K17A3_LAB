thi_sinh = {
    280: {'Họ và tên': 'Nguyễn Thị Ngọc Huyền', 'Điểm thi': 10},
    114: {'Họ và tên': 'Trần Hữu Việt', 'Điểm thi': 7},
    240: {'Họ và tên': 'Lương Trần Ngọc Phúc', 'Điểm thi': 9},
    230: {'Họ và tên': 'Giang Xuân Bảo', 'Điểm thi': 8}
}

while True:
    print('\n1. Tra cứu điểm thi')
    print('2. Thêm thông tin thí sinh')
    print('3. Thoát')

    choice = input('Nhập lựa chọn của bạn: ')

    if choice == '1':
        sbd = int(input('Nhập số báo danh của thí sinh: '))
        if sbd in thi_sinh:
            print(f'Họ và tên: {thi_sinh[sbd]['Họ và tên']}, Điểm thi: {thi_sinh[sbd]['Điểm thi']}')
        else:
            print('Số báo danh không tồn tại.')
    elif choice == '2':
        sbd = int(input('Nhập số báo danh của thí sinh: '))
        if sbd in thi_sinh:
            print('Số báo danh đã tồn tại.')
        else:
            ten = input('Nhập họ và tên của thí sinh: ')
            diem = int(input('Nhập điểm thi của thí sinh: '))
            thi_sinh[sbd] = {'Họ và tên': ten, 'Điểm thi': diem}
            print('Đã thêm thông tin của thí sinh.')
    elif choice == '3':
        break
    else:
        print('Lựa chọn không hợp lệ. Vui lòng chọn lại.')
