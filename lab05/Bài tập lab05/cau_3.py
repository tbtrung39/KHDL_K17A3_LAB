n = int(input("Nhập số tự nhiên n: "))
while n < 0:
    n = int(input("n phải là số tự nhiên! Yêu cầu nhập lại n: "))
he_nhi_phan = ""
if n == 0:
    he_nhi_phan = "0"
while n > 0:
    a = n % 2
    he_nhi_phan = str(a) + he_nhi_phan
    n //= 2
print(f"Số nhị phân của {n} là: {he_nhi_phan}")
