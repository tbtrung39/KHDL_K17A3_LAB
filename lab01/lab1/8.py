# Nhập tọa độ của 3 đỉnh A, B, C của tam giác
Ax = float(input("Nhập tọa độ x của điểm A: "))
Ay = float(input("Nhập tọa độ y của điểm A: "))

Bx = float(input("Nhập tọa độ x của điểm B: "))
By = float(input("Nhập tọa độ y của điểm B: "))

Cx = float(input("Nhập tọa độ x của điểm C: "))
Cy = float(input("Nhập tọa độ y của điểm C: "))


Tx = (Ax + Bx + Cx) / 3
Ty = (Ay + By + Cy) / 3

print("Tọa độ của trọng tâm là: (", round(Tx, 2), ",", round(Ty, 2), ")")
