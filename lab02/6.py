a=int(input('nhap so nguyen co 3 chu so: '))
a1=a//100
a2=(a//10)%10
a3=a%10
if a1==1:
    a1='Mot tram'
elif a1==2:
    a1='Hai tram'
elif a1==3:
    a1='ba tram'
elif a1==4:
    a1='bon tram'
elif a1==5:
    a1='nam tram'
elif a1==6:
    a1='Sau tram'
elif a1==7:
    a1='bay tram'
elif a1==8:
    a1='Tam tram'
elif a1==9:
    a1='chin tram'
#.d.d.d
if a2==1:
    a2='muoi'
elif a2==2:
    a2='Hai muoi'
elif a2==3:
    a2='ba muoi'
elif a2==4:
    a2='bon muoi'
elif a2==5:
    a2='nam muoi'
elif a2==6:
    a2='Sau muoi'
elif a2==7:
    a2='bay muoi'
elif a2==8:
    a2='Tam muoi'
elif a2==9:
    a2='chin muoi'
elif a2==0 and a3!=0:
    a2='le'
else:
    a2=''
if a3==1:
    a3='mot'
elif a3==2:
    a3='Hai'
elif a3==3:
    a3='ba'
elif a3==4:
    a3='bon'
elif a3==5:
    a3='nam'
elif a3==6:
    a3='Sau'
elif a3==7:
    a3='bay'
elif a3==8:
    a3='Tam'
elif a3==9:
    a3='chin'
elif a3==0:
    a3=''
print('cac doc {a} la:',a1+' '+a2+' '+a3)
