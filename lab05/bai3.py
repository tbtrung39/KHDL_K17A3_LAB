#3. Nhập một số tự nhiên n từ bàn phím. Viết chương trình chuyển số n từ hệ cơ số 10 sang nhị phân. Kết quả là chuỗi nhị phân.
n = int(input("Nhập một số nguyên dương n: "))
chuoi = ""
while n > 0:
    chuoi = str(n%2) + chuoi
    n = n//2
print("kết quả là:",chuoi)