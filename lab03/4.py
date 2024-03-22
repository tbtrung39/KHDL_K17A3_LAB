chieu_rong = 5
chieu_dai = 3
for i in range(chieu_dai):
    if i == 0 or i == chieu_dai - 1:
        print("*" * chieu_rong)
    else:
        print("*" + "*" * (chieu_rong - 2) + "*")