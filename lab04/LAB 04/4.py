tu_so = int(input('Nhap tu so: '))
mau_so = False

while mau_so == False:
    mau_so= int(input('Nhap mau so: '))
    if mau_so == 0:
        print('Nhap lai mau so: ')
    else:
        print("phan so co dang: ", tu_so,"/",mau_so) 
           