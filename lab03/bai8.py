print("phần a.")
n = int(input("nhập n: "))
tong = 0
for i in range(1, n+1):
    if n <= 0:
        continue
    else:
        tong+=i
print("S1=", tong)

print("phần b.")
n = int(input("nhập n: "))
tong = 0
for i in range(1, (2*n)+1, 2):
    if n <= 0:
        continue
    else:
        tong+=i
print("S2=", tong)

print("phần c.")
n = int(input("nhập n: "))
tong = 0
for i in range(2, (2*n), 2):
    if n <= 0:
        continue
    else:
        tong+=i
print("S3=", tong)