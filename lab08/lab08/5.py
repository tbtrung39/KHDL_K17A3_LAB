def ucln():
    a=int(input('nhập số a:'))
    b=int(input('nhập số b:'))
    uoc_a=[]
    uoc_b=[]
    for i in range(1,a+1):
        if a%i==0:
            uoc_a.append(i)
    for i in range(1,b+1):
        if b%i==0:
            uoc_b.append(i)        
    uoc_chung_ln=1
    for i in uoc_a:
        if i in uoc_b:
            uoc_chung_ln=i
    print('vậy ước chung lớn nhất của hai số là:',uoc_chung_ln)
    return
ucln()