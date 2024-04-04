a=float(input("nhap mot so:"))
b=float(input("nhap mot so:"))
c=float(input("nhap mot so:"))
x_dinh=-b/(2*a)
y_dinh=a*x_dinh**2+b*x_dinh+c
bac_hai=round(x_dinh,2)
bac_hai=round(y_dinh,2)
print("diem dinh phuong trinh co x={x_dinh},y={y_dinh}")
