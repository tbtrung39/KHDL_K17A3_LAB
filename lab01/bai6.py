Ax, Ay = input("nhap toa do dinh A: ").split()
Ax, Ay = float(Ax),float(Ay)

Bx, By = input("nhap toa do dinh B: ").split()
Bx, By = float(Bx),float(By)

Cx, Cy = input("nhap toa do dinh C: ").split()
Cx, Cy = float(Cx),float(Cy)

T_x = (Ax + Bx + Cx) / 3
T_y = (Ay + By + Cy) / 3
print(f"toa do trong tam tam giac la: {round(T_x,2)},{round(T_y,2)}")