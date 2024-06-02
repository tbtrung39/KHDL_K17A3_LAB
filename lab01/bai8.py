x1, y1 = map(float, input("Nhập tọa độ đỉnh A: ").split())
x2, y2 = map(float, input("Nhập tọa độ đỉnh B: ").split())
x3, y3 = map(float, input("Nhập tọa độ đỉnh C: ").split())
trong_tam = f"{(x1+x2+x3)/3:.2f}" , f"{(y1+y2+y3)/3:.2f}"
print("Tọa độ trọng tâm là: ", trong_tam)