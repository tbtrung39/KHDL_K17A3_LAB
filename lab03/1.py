n = int(input("Nhập n:"))

bt = 2 * (n + 1) / (2 * n + 3)

ps = 1 / 3
for i in range(n):
    ps *= (2 * (i + 1) + 2) / (2 * (i + 1) + 3)

ket_qua = bt / ps

lam_tron = "{:.3f}".format(ket_qua)

print (lam_tron)