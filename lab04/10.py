n=int(input("Nhập vào một số:"))
ket_qua=""
while n>0:
    so=n%10
    if so==0:
        chu='khong'
    elif so==1:
        chu='mot'
    elif so==2:
        chu='hai'
    elif so==3:
        chu='ba'
    elif so==4:
        chu='bon'
    elif so==5:
        chu='nam'
    elif so==6:
        chu='sáa'
    elif so==7:
        chu='bay'
    elif so==8:
        chu='tam'
    else:
        chu='chin'
    ket_qua=chu+" "+ket_qua
    n=n//10
print(ket_qua.strip())