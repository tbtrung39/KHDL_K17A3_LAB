n = int(input("nhập số nguyên dương n là: "))

for so in range(2, n + 1):
    if all(so % i != 0 for i in range(2, int(so ** 0.5) + 1)):
        print(so)