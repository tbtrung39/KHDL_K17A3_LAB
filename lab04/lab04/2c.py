n=int(input('nhập số n ='))
if n<=0:
    print("nhập lại")
else:
    tong=0
    i=2
    while i<=n:
        tong = tong +1/(i**(1/2))
        i=i+1
        print("tổng của dãy là",(tong))