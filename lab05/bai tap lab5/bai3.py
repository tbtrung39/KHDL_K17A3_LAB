# Chuyển số tự nhiên từ hệ 10 sang hệ 2
n = int(input("Nhập số tự nhiên:"))
nhi_phan = ""
while n < 0:
    n = input("n phải lớn hơn 0")
while n>0:
    k = n%2
    nhi_phan = str(k) + nhi_phan
    n //=2
print("Chuỗi nhị phân là:", nhi_phan)
