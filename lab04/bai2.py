while True:
    n = int(input("Nhap so"))
    tong=0
    if n<=1:
        print("So da nhap khong hop le")
    else:
     for i in range(1,n+1):
      if i%2==0:
       tong-=1/i
      else:
        tong+=1/i
     print(tong)
     break