a=int(input('Nhập số nguên có 3 chữ số: '))
a1=a//100
a2=(a//10)%10
a3=a%10
if a1==1:
    a1='Một trăm'
elif a1==2:
    a1='Hai trăm'
elif a1==3:
    a1='Ba trăm'
elif a1==4:
    a1='Bốn trăm'
elif a1==5:
    a1='Năm trăm'
elif a1==6:
    a1='Sáu trăm'
elif a1==7:
    a1='Bảy trăm'
elif a1==8:
    a1='Tám trăm'
elif a1==9:
    a1='Chín trăm'
#.d.d.d
if a2==1:
    a2='mươi'
elif a2==2:
    a2='hai mươi'
elif a2==3:
    a2='ba mươi'
elif a2==4:
    a2='bốn mươi'
elif a2==5:
    a2='năm mươi'
elif a2==6:
    a2='sáu mươi'
elif a2==7:
    a2='bảy mươi'
elif a2==8:
    a2='tám mươi'
elif a2==9:
    a2='chín mươi'
elif a2==0 and a3!=0:
    a2='lẻ'
else:
    a2=''
if a3==1:
    a3='một'
elif a3==2:
    a3='hai'
elif a3==3:
    a3='ba'
elif a3==4:
    a3='bốn'
elif a3==5:
    a3='năm'
elif a3==6:
    a3='sáu'
elif a3==7:
    a3='bảy'
elif a3==8:
    a3='tám'
elif a3==9:
    a3='chín'
elif a3==0:
    a3=''
print(f'Cách đọc {a} là',a1+' '+a2+' '+a3)