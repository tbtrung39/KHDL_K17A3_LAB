def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)

def main():
    t1 = int(input('Nhập số thứ 1: '))
    t2 = int(input('Nhập số thứ 2: '))

    if t1 < t2:
        t1, t2 = t2, t1

    gcd = ucln(t1, t2)
    print(f'Ước chung lớn nhất là: {gcd}')

main()
