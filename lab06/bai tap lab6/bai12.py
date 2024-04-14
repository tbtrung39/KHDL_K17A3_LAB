giao_dich=[]
print("__________Nhập nhật ký giao dịch___________")
while True:
    gd=input("Nhập loại giao dịch và số tiền (D/W số_tiền), hoặc nhấn Enter để kết thúc: ")
    if not gd:
        break
    split_gd=gd.split()
    if len(split_gd) != 2:
        print("Lỗi: Chuỗi không đúng định dạng")
        continue
    giao_dich.append((split_gd[0],split_gd[1]))
so_du=0
for loai, so_tien in giao_dich:

    if loai=='D':
        if so_tien.isdigit():
            so_du+=int(so_tien)
        else:
            print("Lỗi: Số tiền phải là một số nguyên")
    elif loai=='W':
        if so_tien.isdigit():
            so_du-=int(so_tien)
        else:
            print("Lỗi: Số tiền phải là một số nguyên")
print("Số tiền thực của tài khoản ngân hàng là: ", so_du)