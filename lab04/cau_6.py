n=int(input('nhâp: '))
a="một "
b="hai "
c='ba '
d='bốn '
e='năm '
f='sáu '
g='bẩy '
h='tám '
k='chín '
m='không '
kt=''
while n>0:
    l=n%10
    print('l:',l)
    n=n//10
    print(n)
    if l==0:
        kt=m+kt
    if l==1:
        kt=a+kt
    if l==2:
        kt=b+kt
    if l==3:
        kt=c+kt
    if l==4:
        kt=d+kt
    if l==5:
        kt=e+kt
    if l==6:
        kt=f+kt
    if l==7:
        kt=g+kt
    if l==8:
        kt=h+kt
    if l==9:
        kt=k+kt
print(kt)