n = int(input("Nhập vào một số nguyên dương: "))
tong_nghich_dao = 0
for i in range(1, n+1):
    tong_nghich_dao += 1/i
print("Tổng nghịch đảo của", n, "số nguyên đầu tiên là:", tong_nghich_dao)