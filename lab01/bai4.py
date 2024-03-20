"""vectoA = int,(input(f"Nhập vecto A: {[]}")).split
vectoB = int,(input(f"Nhập vecto B: {[]}")).split"""
vector1 = input("Nhập vào vector thứ nhất: ")
vector1 = list(map(float, vector1.split()))

# Nhập vào vector thứ hai từ người dùng
vector2 = input("Nhập vào vector thứ hai: ")
vector2 = list(map(float, vector2.split()))


# Tính tích vô hướng
tich_vo_huong = (vector1[0])*(vector2[0]) + (vector1[1])*(vector2[1]) + (vector2[2])*(vector2[2])

print("Tích vô hướng của hai vector là:", tich_vo_huong)
