n = int(input("Nhập số nguyên dương n: "))
print("Các số nguyên tố nhỏ hơn hoặc bằng",n,"là: ")
for i in range(2, n + 1):
    nguyen_to = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            nguyen_to = False
            break        
    if nguyen_to:
        print(i, end=" ")
