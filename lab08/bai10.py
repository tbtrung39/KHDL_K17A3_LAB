def uoc_so(n):
    for i in range(1,n + 1):
        if n % i == 0 :
            print("uoc so la :",i)

n = int(input("nhap so n :"))
uoc_so(n)            