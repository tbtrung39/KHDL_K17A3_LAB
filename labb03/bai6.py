n = int(input("nhập n: "))
tong = 0
for i in range(1, n+1):
    if n <= 0:
        continue
    else:
        tong+=i**3
print("S=", tong)