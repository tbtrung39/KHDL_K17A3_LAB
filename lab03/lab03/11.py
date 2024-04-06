#a)
n = int(input("Nhập số hàng của tam giác: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    else:
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
#b)
h = int(input("Nhập chiều cao của tam giác: "))
for i in range(h):
    if i == 0 or i == h - 1:   
        print(" " * (h - i - 1) + "*" * (2 * i + 1))
    else:
        print(" " * (h - i - 1) + "*" + " " * (2 * i - 1) + "*")

#c)
n = int(input("Nhập chiều cao của tam giác: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()