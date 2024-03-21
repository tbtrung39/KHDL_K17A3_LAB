xA = float(input("Tọa độ x của đỉnh A là: "))
xB = float(input("Tọa độ x của đỉnh B là: "))
xC = float(input("Tọa độ x của đỉnh C là: "))
yA = float(input("Tọa độ y của đỉnh A là: "))
yB = float(input("Tọa độ y của đỉnh B là: "))
yC = float(input("Tọa độ y của đỉnh C là: "))
# gọi G là trọng tâm tam giác 
xG = (xA + xB + xC) /3
yG = (yA + yB + yC) /3
print("Trọng tâm tam giác ABC là: ", round(xG,2) ,";", round(yG,2))