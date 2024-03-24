Dien = float(input("Nhập số KW điện tiêu thụ là: "))
if 0 <= Dien >= 100:
    don_gia=2000
if 101 <= Dien >= 200:
    don_gia=2500  
if 201 <= Dien >= 300:
    don_gia= 3000 
if Dien > 300:
    don_gia=5000   
Tien_dien = Dien*don_gia
print(f"Tiền điện là {Tien_dien} đồng")