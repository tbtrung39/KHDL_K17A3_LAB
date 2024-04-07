a=int(input('nhap thang: '))
b=int(input('nhap ngay: '))
if a==1:
    if b<1 or b>31:
        print('nhap sai ngay')
    else:
        b+=1
        if b>31:
            a=2
            b=1
elif a==2:
    if b<1 or b>28:
        print('nhap sai ngay')
    else:
        b+=1
        if b>28:
            a=3
            b=1
elif a==3:
    if b<1 or b>31:
        print('nhap sai ngay')
    else:
        b+=1
        if b>31:
            a=4
            b=1
elif a==4:
    if b<1 or b>30:
        print('nhap sai ngay')
    else:
        b+=1
        if b>30:
            a=5
            b=1
elif a==5:
    if b<1 or b>31:
        print('nhap sai ngay')
    else:
        b+=1
        if b>31:
            a=6
            b=1
elif a==6:
    if b<1 or b>30:
        print('nhap sai ngay')
    else:
        b+=1
        if b>30:
            a=7
            b=1
elif a==7:
    if b<1 or b>31:
        print('nhap sai ngay')
    else:
        b+=1
        if b>31:
            a=8
            b=1
elif a==8:
    if b<1 or b>30:
        print('nhap sai ngay')
    else:
        b+=1
        if b>31:
            a=9
            b=1
elif a==9:
    if b<1 or b>30:
        print('nhap sai ngay')
    else:
        b+=1
        if b>30:
            a=10
            b=1
elif a==10:
    if b<1 or b>31:
        print('nhap sai ngay')
    else:
        b+=1
        if b>31:
            a=11
            b=1
elif a==11:
    if b<1 or b>30:
        print('nhap sai ngay')
    else:
        b+=1
        if b>30:
            a=12
            b=1
elif a==12:
    if b<1 or b>31:
        print('nhap sai ngay')
    else:
        b+=1
        if b>31:
            a=1
            b=1
print(f'ngay tiep theo la ngay {b} thang {a}')