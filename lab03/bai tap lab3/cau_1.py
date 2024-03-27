n=int(input('Nhập n: '))
tong=1
for i in range(n+1):
    tich=1
    for j in range(i+1):
        tich=tich * (2*(j + 1)) / (2*j + 3)
    tong+=tich
print(round("Tổng của dãy là: ", tong, 3))