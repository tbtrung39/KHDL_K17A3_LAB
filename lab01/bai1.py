a = float(input("nhap chieu cao "))
b = float(input("nhap ban kinh "))
pi = 3.14
s_xung_quanh = round(2*pi*a*b,2)
s_toan_phan = round(s_xung_quanh+(2*pi**(b**2)),2)
the_tich = round(pi*(b**2)*a,2)
print("dien tich xung quanh của khoi tru la :", s_xung_quanh)
print("dien tich toan phan của khoi tru la :", s_toan_phan)
print("the tich cua khoi tru la : ", the_tich)