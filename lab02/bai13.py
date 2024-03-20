print("\nphần c.")
n=int(input("nhập số dòng: "))
print("Ve tam giac sao deu:");
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print("", end = " ");
    for k in range(1, i+1):
        print("*", end=" ");
    print()

print("\nphần a.")
height = int(input("Nhập chiều cao của tam giác: "))
for i in range(height):
    if i == height - 1: 
        print('*' * (2 * height - 1))
    else:
        print(' ' * (height - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))