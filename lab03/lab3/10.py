n = int(input('Nhập vào một giá trị nguyên dương: '))
a = []

thuong = 2
for thuong in range(1, n+1):
    if n % thuong == 0:
        a.append(thuong)
        n //= thuong
        thuong -=1

tich_thuong = 1
for a in a:
    tich_thuong *= a

print(f'Tích thương các số nguyên tố của {n} là: {tich_thuong}')