# Hóa
x=float(input('nhập số gam Al2O3:'))
y=float(input('nhập khối lượng mol(M) của NaOH:'))
z=float(input('nhập khối lượng mol(M) của HCl:'))
if 0.1*y-0.02*x>0.1*z: 
    print('sau phản ứng có kết tủa')
else:
    print('sau phản ứng không có kết tủa')