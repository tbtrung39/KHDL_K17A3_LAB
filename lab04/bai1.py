while True:
    i=int(input("Nhap so"))
    result=0
    if i<=0:
        print("Ki tu khong hop le")
    else:
        for n in range(0,i+1):
         result+=n**2
    print(result)