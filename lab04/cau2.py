n=int(input('nhap n: '))
sa=0
i=1
while i<=n:
    if i%2!=0:
        sa+=1/i
    else:
        sa+=-1/i
    i+=1
sb=0
sc=0
i=1
while i<=n:
    sb+=1/(i*(i+1))
    i+=1 
i=2
while i<=n+1:
    sc+=1/(i**0.5)
    i+=1
print(f'sa={sa}, sb={sb}, sc={sc}')