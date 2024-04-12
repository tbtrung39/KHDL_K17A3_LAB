
D=0
while True:
    print('chọn chức năng:')
    print('1. Gửi tiền')
    print('2. Rút tiền')
    print('3. Kiểm tra số tiền trong tài khoản')
    choose = int(input('chọn chức lăng: '))
    while choose not in [1,2,3]:
        print('chọn lại chức năng!')
    if choose == 1:
        t=int(input('nhập số tiền gửi: '))
        D+=t
    if choose == 2:
        if D==0:
            print('tài khoản hiện tại không có tiền để rút ạ!')
        else:
            t=int(input('nhập số tiền muốn rút: '))
        while t>D:
            print(f'số tiền muốn rút lớn hơn só tiền hiện có(số dư : {D})')
            t=int(input('nhập lại số tiền muốn rút: '))
        D-=t
    if choose == 3:
        print(f'Số tiền hiện tại còn trong tài khoản là: {D}')
    tt= input('bạn có muốn tiếp tục hay không?(y/n): ').strip().lower()
    if tt == 'n':
        break
