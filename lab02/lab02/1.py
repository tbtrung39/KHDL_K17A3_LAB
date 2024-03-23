a = int(input("Nhap vao mot thang: "))
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a== 10 or a ==12:
    print(f'Thang {a} co 31 ngay.')
elif a == 4 or a ==6 or a == 9 or a ==11:
    print(f'Thang {a} co 30 ngay.')
elif a == 2:
    print(f'Thang {a} co 28 ngay.')
else:
    print('Khong hop le')