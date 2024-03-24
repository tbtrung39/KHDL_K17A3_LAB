
x = float(input("Nhập giá trị của x: "))
y = float(input("Nhập giá trị của y: "))
z = float(input("Nhập giá trị của z: "))

n_Al2O3 = x/(162.0)
n_NaOH = y*100/1000
n_HCl = z*100/1000


n_Al3 = 2*n_Al2O3
n_O2 = 3*n_Al2O3
n_Na = n_NaOH
n_OH = n_NaOH
n_H = n_HCl
n_Cl = n_HCl

if n_Al3 + n_OH > n_Na + n_Cl:
    print("Sau phản ứng có kết tủa")
else:
    print("Sau phản ứng không có kết tủa")
