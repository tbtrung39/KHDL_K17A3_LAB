n = int(input('Nhập vào số tự nhiên n: '))
a = set()
b = set()
for i in range(1, n+1):
    if n%i == 0:
        nto = True
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                nto= False
                break
            if nto:
                a.add(i)
        else:
            nto = True
            for j in range(2, int(i**0.5)+1):
                if i%j == 0:
                    break
                if nto:
                    b.add(i)
                    print(f'Tập hợp A: {a}')
                    print(f'Tập hợp B: {b}')