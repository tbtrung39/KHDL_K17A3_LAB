# Viết chương trình tìm các số hoàn hảo nhỏ hơn n (với n được nhập từ bàn phím).
n=int(input("Nhập số n: "))
for so in range(1,n):
    s=0
    for i in range(1, so):
        if (so%i==0):
            s+=i
    if s==so:
        print(so)