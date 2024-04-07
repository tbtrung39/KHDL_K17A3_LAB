chuoi = input("Nhập vào một chuỗi: ")
chuoi_moi = ""
for c in chuoi:
    if "0" <= c <= "9":
        chuoi_moi +=c
print("Kết quả của chuỗi khi xóa hết chữ là số",chuoi_moi)   

tong = 0    
for i in range(1,int(chuoi_moi)):
    if int(chuoi_moi) % i == 0 :
            tong += i
if tong == int(chuoi_moi):
    print("Số",chuoi_moi,"là số hoàn hảo")
else:
    print("Số",chuoi_moi,"không phải là số hoàn hảo")