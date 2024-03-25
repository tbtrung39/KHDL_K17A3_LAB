n=int(input("Nhập vào một số:"))
ket_qua=""
while n>0:
    so=n%10
    if so==0:
        chu='không'
    elif so==1:
        chu='một'
    elif so==2:
        chu='hai'
    elif so==3:
        chu='ba'
    elif so==4:
        chu='bốn'
    elif so==5:
        chu='năm'
    elif so==6:
        chu='sáu'
    elif so==7:
        chu='bảy'
    elif so==8:
        chu='tám'
    else:
        chu='chín'
    ket_qua=chu+" "+ket_qua
    n=n//10
print(ket_qua.strip())