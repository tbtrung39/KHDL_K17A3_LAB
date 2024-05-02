n = int(input("nhap 1 so tu nhien :"))
a = set()
b = set()
for i in range(1,n+1):
    if n == 0 :
        nto = True
        for j in range(2,int(i**0.5) + 1):
            if i % j ==0:
                nto = False
                break
            if nto:
                a.add(i)
        else:
            nto = True
            for  j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
                if nto:
                    b.add(i)
                    print(f'tap hop a : {a}')
                    print(f'tap hop b : {b}')
                            
            