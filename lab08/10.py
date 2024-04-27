def uoc_so(n):
    uocs=[]
    for i in range(1, n+1):
        if n%i==0:
            uocs.append(i)
    return uocs 
n=int(input("Nhập số nguyên dương n: "))
print("Các ước số của", n, "là:", uoc_so(n))