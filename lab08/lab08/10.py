def uoc():
    n=int(input('nhập số n ='))
    for i in range(1,n+1):
        if n%i==0:
            print('các ước của nó là:',i)
    return
uoc()