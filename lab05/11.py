
chuoi_nhi_phan=input("Nhập chuỗi ký tự nhị phân: ")
so_thap_phan=0
for i in range(len(chuoi_nhi_phan)):
    so_thap_phan+=int(chuoi_nhi_phan[i])*(2**(len(chuoi_nhi_phan)-1-i))
print("Số thập phân tương ứng của chuỗi nhị phân {} là: {}".format(chuoi_nhi_phan,so_thap_phan))
