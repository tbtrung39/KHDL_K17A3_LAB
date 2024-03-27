n = int(input("nhập n: "))
s=0
for i in range(1, n):
    s+= 1/i
print(f"tổng {n} số đầu tiên là: {s}")