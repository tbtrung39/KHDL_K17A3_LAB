n = int(input( " nhập số n"))
ket_qua=1
tinh_bieu_thuc=1
for i in range(1,n+1):
    tinh_bieu_thuc *=(2*i)/((2*i)+1)
    ket_qua += tinh_bieu_thuc
print(round(ket_qua,3))