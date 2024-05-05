def ucln(a,b):
    if b==0:
        return a
    return ucln(b,a%b)
def bcnn(a,b):
    return int(a*b/ucln(a,b))
a,b=map(int,input('nhập 2 số a,b cách nhau bởi dấu cách: ').split())
print(f'bội chung nhỏ nhất của {a},{b} là: {bcnn(a,b)}')