n=int(input("Nhập số nguyên dương n: "))
uoc_so_nguyen_to=set()
nguyen_to_nho_hon_n=set()
for i in range(2, n+1):
    if n%i==0:
        nguyen_to=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                nguyen_to=False
                break
            if nguyen_to:
                uoc_so_nguyen_to.add(i)
for i in range(2, n):
    if i not in uoc_so_nguyen_to:
        nguyen_to=True
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                nguyen_to=False
                break
            if nguyen_to:
                nguyen_to_nho_hon_n.add(i)
print("Tập hợp các số nguyên tố là ước của n: ", uoc_so_nguyen_to)
print("Tập hợp các số nguyên tố nhỏ hơn n và không là ước của n: ", nguyen_to_nho_hon_n)

