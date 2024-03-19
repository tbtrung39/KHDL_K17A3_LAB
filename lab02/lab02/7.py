diem_TK = int(input('Nhap so diem: '))
if diem_TK >= 0 and diem_TK<= 3:
    print('Kem')
elif diem_TK == 4:
    print("Yeu")
elif diem_TK >= 5 and diem_TK <=6:
    print('TB')
elif diem_TK >= 7 and diem_TK <=8:
    print('Kha')
elif diem_TK >= 9 and diem_TK <=10 :
    print('Gioi')
else: 
    print('Nhap lai')