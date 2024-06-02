y=int(input('nhập năm:'))
m=int(input('nhập tháng:'))
def nhuan(y):
    if y%400==0 or (y%4==0 and y%100!=0):
        return True
    else:
        return False
def thang(a):
    if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
        print(f'tháng {a} có 31 ngày')
    if a==4 or a==6 or a==9 or a==11:
        print(f'tháng {a} có 30 ngày') 
    if a==2:
        if nhuan(y):
            print(f'tháng {a} có 28 ngày')
        else:
            print(f'tháng {a} có 29 ngày')

if nhuan(y):
    print(f'năm {y} là năm nhuận')
else:
    print(f'năm {y} là năm không nhuận')
thang(m)