import re 
mat_khau_nhap=input("Nhập các mật khẩu, phân tách bởi dấu phẩy: ").split(',')
mat_khau_hop_le=[]
for mat_khau in mat_khau_nhap:
    if len(mat_khau) < 6 or len(mat_khau)>12:
        continue
    if not re.search("[a-z]", mat_khau):
        continue
    if not re.search("[A-Z]", mat_khau):
        continue
    if not re.search("[0-9]", mat_khau):
        continue
    if not re.search("[$#@]", mat_khau):
        continue
    mat_khau_hop_le.append(mat_khau)
print(','.join(mat_khau_hop_le))