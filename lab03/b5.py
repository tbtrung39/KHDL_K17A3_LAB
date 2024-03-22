width = int(input("Nhập chiều rộng của hình chữ nhật: "))
height = int(input("Nhập chiều cao của hình chữ nhật: "))
print("Hình chữ nhật:")
for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print("*", end="")
        else:
            print("*", end="")
    print()