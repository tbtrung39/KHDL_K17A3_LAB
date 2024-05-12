def luy_thua_cua_mot_so(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / luy_thua_cua_mot_so(a, -b)
    else:
        return a * luy_thua_cua_mot_so(a, b - 1)

def main():
    a = int(input('Nhập số: '))
    b = int(input('Nhập số mũ: '))
    
    result = luy_thua_cua_mot_so(a, b)
    
    print(f'Kết quả của phép lũy thừa là: {result}')

main()
