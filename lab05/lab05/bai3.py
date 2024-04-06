n = int(input("Nhập một số nguyên dương n: "))
chuoi = ""
while n > 0:
    chuoi = str(n%2) + chuoi
    n = n//2
print("kết quả là:",chuoi)