n=float(input("Nhap so dien tieu thu: "))
if n>0 and n<=100:
    gia_dien=2000
elif n>=101 and n<=200:
    gia_dien=2500
elif n>=201 and n<= 300:
    gia_dien =3000
elif n>=300:
    gia_dien=5000
tien_dien=n*gia_dien
print(f"Tien dien can thanh toan la: tien_dien={tien_dien}")