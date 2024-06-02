def tim_uoc_so(a):
    uoc_so = []
    for i in range(1,a+1):
        if a % i ==0:
            uoc_so.append(i)
    return uoc_so

n = int(input("Nhập số: "))
uoc_so = tim_uoc_so(n)
print(uoc_so)