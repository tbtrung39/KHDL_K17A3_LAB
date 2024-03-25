# Nhập vào số hàng của tam giác
n = int(input("Nhập vào số hàng của tam giác: "))

print("Tam giác cân rỗng:")
for i in range(n):
    for j in range(n - i - 1):
        print(end=" ")
    for j in range(2*i + 1):
        if j == 0 or j == 2*i or i == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\nTam giác đều rỗng:")
for i in range(n):
    for j in range(n - i - 1):
        print(end=" ")
    for j in range(2*i + 1):
        if j == 0 or j == 2*i or i == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\nTam giác đặc:")
for i in range(n):
    for j in range(n - i - 1):
        print(end=" ")
    for j in range(2*i + 1):
        print("*", end="")
    print()
