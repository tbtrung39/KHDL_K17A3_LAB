
thang=int(input('Nhập tháng: '))
ngay=int(input('Nhập ngày: '))
if thang==1:
    if ngay<1 or ngay>31:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>31:
            thang=2
            ngay=1
elif thang==2:
    if ngay<1 or ngay>28:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>28:
            thang=3
            ngay=1
elif thang==3:
    if ngay<1 or ngay>31:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>31:
            thang=4
            ngay=1
elif thang==4:
    if ngay<1 or ngay>30:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>30:
            thang=5
            ngay=1
elif thang==5:
    if ngay<1 or ngay>31:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>31:
            thang=6
            ngay=1
elif thang==6:
    if ngay<1 or ngay>30:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>30:
            thang=7
            ngay=1
elif thang==7:
    if ngay<1 or ngay>31:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>31:
            thang=8
            ngay=1
elif thang==8:
    if ngay<1 or ngay>30:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>31:
            thang=9
            ngay=1
elif thang==9:
    if ngay<1 or ngay>30:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>30:
            thang=10
            ngay=1
elif thang==10:
    if ngay<1 or ngay>31:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>31:
            thang=11
            ngay=1
elif thang==11:
    if ngay<1 or ngay>30:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>30:
            thang=12
            ngay=1
elif thang==12:
    if ngay<1 or ngay>31:
        print('Nhập sai ngày')
    else:
        ngay+=1
        if ngay>31:
            thang=1
            ngay=1
print(f'Ngày tiếp theo là ngày {ngay} tháng {thang}')
