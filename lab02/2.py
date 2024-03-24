a = int(input('nhap gia tri a : '))
b = int(input('nhap gia tri b : '))
c = int(input('nhap gia tri c : '))
delta = b**2 - 4*a*c
can_delta = delta **0.5
if delta < 0 :
    print('phuong trinh vo nghiem ')
elif delta == 0 :
    print('phuong trinh co nghiem kep : x1=x2=',-b/2*a)
elif delta >0:
    print('phuong trinh co 2 nghiem phan biet','x1=',(-b/can_delta)/2*a,'x2 =',(b+can_delta)/2*a)
