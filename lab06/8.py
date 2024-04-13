n = int(input("Nhập số nguyên dương n: "))
fibonacci = [0, 1] + [fibonacci[i-1] + fibonacci[i-2] for i in range(2, n)]
a = ",".join(map(str, fibonacci))
print(a)
