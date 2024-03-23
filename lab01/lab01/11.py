n = int(input("Nhập số lần tung xúc sắc: "))
khong_ra_6 = (5/6) ** 3 
khong_co_lan_nao_ra_6 = khong_ra_6 ** n 
it_nhat_1_lan_ra_6 = 1 - khong_co_lan_nao_ra_6 
print("Xác suất khi tung n lần 3 xúc sắc có ít nhất 1 lần cả 3 ra 6: ", round(it_nhat_1_lan_ra_6, 2))