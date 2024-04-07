n=int(input('nhập số n ='))
if n<=0:
    print("nhập lại")
else:
    tong=0
    i=1
    while i<=n+1:
        tong = tong +(2*i+1)**3
        i=i+1
        print("tổng của dãy là",(tong))