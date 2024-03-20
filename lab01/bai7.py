def toa_do_trong_tam(x1, y1, x2, y2, x3, y3):
    # Tính tọa độ trọng tâm
    x = (x1 + x2 + x3) / 3
    y = (y1 + y2 + y3) / 3

    return x, y

# Nhập tọa độ của 3 đỉnh A, B, C
x1, y1 = map(float, input("Nhập tọa độ đỉnh A (x1 y1): ").split())
x2, y2 = map(float, input("Nhập tọa độ đỉnh B (x2 y2): ").split())
x3, y3 = map(float, input("Nhập tọa độ đỉnh C (x3 y3): ").split())

# Tính trọng tâm của tam giác
trong_tam = toa_do_trong_tam(x1, y1, x2, y2, x3, y3)

# In ra kết quả
print(f"Tọa độ trọng tâm của tam giác là: {trong_tam}")
