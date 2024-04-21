n = int(input("Nhập số bậc n của ma trận đơn vị: "))
ma_tran_don_vi = []

# Tạo ma trận đơn vị bậc n
for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang.append(1)
        else:
            hang.append(0)
    ma_tran_don_vi.append(hang)

# In ma trận đơn vị
print("Ma trận đơn vị bậc", n, ":")
for hang in ma_tran_don_vi:
    print(hang)