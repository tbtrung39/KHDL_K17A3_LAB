#Viết chương trình nhập vào 2 vector a và b. Tính tích vô hướng của 2 vector đó
Ax, Ay = input("nhap toa do vecto A: ").split()
Ax, Ay = float(Ax),float(Ay)

Bx, By = input("nhap toa do veto B: ").split()
Bx, By = float(Bx),float(By)

tich_vo_huong = Ax*Bx + Ay*By
print("tich vo huong cua 2 vecto la: ", tich_vo_huong)