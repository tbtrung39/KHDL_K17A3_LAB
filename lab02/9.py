n=int(input("Nhập số KW tiêu thụ:"))
if  n>0 and n<100:
    don_gia=2000
elif n >101 and n<200:
    don_gia=2500
elif n >201 and n<300:
    don_gia=3000
else:
    don_gia=5000
tien_dien=n*don_gia
print("Tiền điện : ",tien_dien,"đồng")