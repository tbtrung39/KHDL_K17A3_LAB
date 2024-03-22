Ax, Ay=map(float,input("Nhap toa do dinh A (x,y): ").split(","))
Bx, By=map(float,input("Nhap toa do dinh B (x,y): ").split(","))
Cx, Cy=map(float,input("Nhap toa do dinh C (x,y): ").split(","))
Tx= (Ax+Bx+Cx)/3
Ty= (Ay+By+Cy)/3
print("Toa do trong tam cua tam giac la: ({:.2f}, {:.2f})".format(Tx,Ty))