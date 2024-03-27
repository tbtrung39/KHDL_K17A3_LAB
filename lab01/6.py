# Nhập tọa độ của ba đỉnh A, B, C từ bàn phím
Ax,Ay = map(float, input("Nhập tọa độ của đỉnh A (cách nhau bởi dấu cách): ").split())
Bx,By = map(float, input("Nhập tọa độ của đỉnh B (cách nhau bởi dấu cách): ").split())
Cx,Cy = map(float, input("Nhập tọa độ của đỉnh C (cách nhau bởi dấu cách): ").split())

# Tính tọa độ của trọng tâm
Gx = (Ax + Bx + Cx) / 3
Gy = (Ay + By + Cy) / 3

# In kết quả
print("Trọng tâm của tam giác là: ({:.2f}, {:.2f})".format(Gx, Gy))