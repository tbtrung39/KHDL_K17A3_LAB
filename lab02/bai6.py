so = int(input("nhap so nguyen co ba chu so: "))
a1 = so // 100
a2 = (so //10)%10
a3 = so %10
if a1 == 1:
    a1 ='mot tram'
elif a1 == 2:
    a1 ='hai tram'
elif a1 == 3:
    a1 ='ba tram'
elif a1 == 4:
    a1 ='bon tram'
elif a1 == 5:
    a1 ='nam tram'
elif a1 == 6:
    a1 ='sau tram'
elif a1 == 7:
    a1 ='bay tram'
elif a1 == 8:
    a1 ='tam tram'
elif a1 == 9:
    a1 ='chin tram'

if a2 ==1:
    a2='muoi'
elif a2==2:
    a2='hai muoi'
elif a2==3:
    a2='ba muoi'
elif a2==4:
    a2='bon muoi'
elif a2==5:
    a2='nam muoi'
elif a2==6:
    a2='sau muoi'
elif a2==7:
    a2='bay muoi'
elif a2==8:
    a2='tam muoi'
elif a2==9:
    a2='chin muoi'

if a3 ==1:
    a3='mot'
elif a3 == 2:
    a3='hai'    
elif a3 == 3:
    a3='ba' 
elif a3 == 4:
    a3='bon' 
elif a3 == 5:
    a3='nam' 
elif a3 == 6:
    a3='sau' 
elif a3 == 7:
    a3='bay' 
elif a3 == 8:
    a3='tam' 
elif a3 == 9:
    a3='chin' 
elif a3 == 0:
    a3='' 
print(f"so {so} co cach doc la: {a1 + a2 + a3}")