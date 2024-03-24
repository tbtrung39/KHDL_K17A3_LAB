n = int(input("Nhập số lần tung xúc sắc: "))
# Xác suất không ra 6 khi tung một xúc sắc là 5/6
# Do đó, xác suất không cả 3 xúc sắc ra 6 là (5/6) ^ 3
p_khong_ra_6 = (5/6) ** 3

# Xác suất không có lần nào cả 3 xúc sắc ra 6 sau n lần tung là (p_khong_ra_6) ^ n
p_khong_co_lan_nao_ca_3_ra_6 = p_khong_ra_6 ** n

# Xác suất có ít nhất một lần cả 3 xúc sắc ra 6 là 1 trừ đi xác suất không có lần nào cả 3 xúc sắc ra 6
p_it_nhat_1_lan_ca_3_ra_6 = 1 - p_khong_co_lan_nao_ca_3_ra_6

print(f"Xác suất khi tung {n} lần 3 xúc sắc có ít nhất 1 lần cả 3 ra 6 là: {p_it_nhat_1_lan_ca_3_ra_6:.2f}")