n = int(input("Nhập số nguyên dương n: "))
print("Các số hoàn hảo nhỏ hơn", n, "là:")
for k in range(2, n):
    z = 0
    for i in range(1, k):
        if k % i == 0:
            z += i
    if z == k:
        print(k)

