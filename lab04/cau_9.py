n=int(input('nhập số:'))
tong=0
while n>0:
    l=n%10
    tong+=l
    n//=10
print('tổng của các chữ số vừa nhập là:',tong)
