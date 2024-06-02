n = int(input("nhập số nguyên n:"))
k = 0
for i in range(1, n + 1):
    k += i ** 3
print("tổng bậc 3 của",n,"số nguyên đầu là:",k)