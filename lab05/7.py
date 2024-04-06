
chuoi=input("Nhập chuỗi ký tự: ")
so=" "
for ky_tu in chuoi:
    if ky_tu.isdigit():
        so+=ky_tu
print("Chuỗi số sau khi loại bỏ ký tự không phải số:", so)
if not so:
    print("Chuỗi không chứa số nào")
else:
    so_nguyen=int(so)
    tong_uoc=sum([i for i in range(1,so_nguyen) if so_nguyen% i==0])
    if tong_uoc == so_nguyen:
        print("Chuỗi số là số hoàn hảo")
    else:
        print("Chuỗi số không phải số hoàn hảo")
