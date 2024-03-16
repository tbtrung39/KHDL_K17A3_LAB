n = int(input("Nhập số lần tung xúc sắc: "))
mat_6 = 1/6
print("Xác suất xúc sắc có một mặt là 6 trong một lần gieo là: ", mat_6)
mat_khac_6 = 5/6
print("Xác suất xúc sắc có một mặt khác 6 trong một lần gieo là: ", mat_khac_6)
ba_mat_khac_6 = (mat_khac_6)**3
print("Xác suất xúc sắc có ba mặt khác 6 trong một lần gieo là :", ba_mat_khac_6)
n_lan_ba_mat_khac_6 = (ba_mat_khac_6)**n
print("Xác suất xúc sắc có ba mặt khác 6 trong n lần gieo là: ", n_lan_ba_mat_khac_6)
mot_lan_ba_mat_6 = 1 - n_lan_ba_mat_khac_6
print("Xác suất để tung", n, "lần 3 xúc sắc có ít nhất 1 lần cả 3 mặt ra 6 là: ", f"{mot_lan_ba_mat_6:.2f}")