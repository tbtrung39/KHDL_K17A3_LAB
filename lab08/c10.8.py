def tim_uoc(n):
    cac_uoc=[]
    for i in range(1,n):
        if n%i == 0:
            cac_uoc.append(i)
    return cac_uoc

n=int(input("nhập số nguyên dương: "))
uoc= tim_uoc(n)
print(f"các ước của {n} là: {uoc}")
