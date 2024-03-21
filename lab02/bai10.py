gio_bd = float(input("nhap gio bat dau: "))
gio_kt = float(input("nhap gio ket thuc: "))
if gio_bd < 5 and gio_kt > 22 or gio_bd>gio_kt:
    print("")
elif gio_bd >=11 and gio_kt <=15:
    if (gio_kt - gio_bd) >=3:
        tien = ((3*100000) + (((gio_kt - gio_bd-3)*100000)*0.75))*0.9
        print(tien)
    else:
        tien = ((gio_kt-gio_bd)*100000)*0.9
        print(tien)
else:
    if (gio_kt-gio_bd) >=3:
        tien = ((3*100000) + (gio_kt-gio_bd-3)*100000)*0.75
    else:
        tien = (gio_kt-gio_bd)*100000
    print(tien)