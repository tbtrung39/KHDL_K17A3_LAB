def bcnn():
    a=int(input('nhập số a ='))
    b=int(input('nhập số b ='))
    boi_a=[]
    boi_b=[]
    for i in range(1,b+1):
        boi_a.append(a*i)
    for i in range(1,a+1):
        boi_b.append(b*i)
    boi_cnn=min(set(boi_a)&set(boi_b))
    print('bội chung nhỏ nhất là :',boi_cnn)
    return
bcnn()