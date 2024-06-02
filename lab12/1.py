while True:
    while True:
        try:
            a=float(input('nhap a: '))
            assert a>0, 'phai nhap so lon hon 0'
        except ValueError:
            print('phai nhap so!')
        break
    while True:
        try:
            b=float(input('nhap b: '))
            assert b>0, 'phai nhap so lon hon 0'
        except ValueError:
            print('phai nhap so!')
        break
    while True:
        try:
            c=float(input('nhap c: '))
            assert c>0, 'phai nhap so lon hon 0'
        except ValueError:
            print('phai nhap so!')
        break
    assert a+b>c and a+c>b and b+c>a, 'khong thoa man dieu kien cua tam giac'
    break

        