a = int(input("Nhập vào số a:"))
b = int(input("Nhập vào số b:"))
def tinh(a,b):
    cong = a+b
    hieu = a-b
    tich = a*b
    chia = a/b
    return cong,hieu,tich,chia
cong,hieu,tich,chia = tinh(a,b)
print("Tổng của hai số là:",cong)
print("Hiệu của hai số là:",hieu)
print("Tích của hai số là:",tich)
print("Thương của hai số là:",chia)