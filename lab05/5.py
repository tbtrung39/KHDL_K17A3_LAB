
Str=input("Nhập chuỗi ký tự: ")
chuoi_so=" "
for ch in Str:
    if ch.isdigit():
        chuoi_so+=ch
if chuoi_so:
    so=int(chuoi_so)
    print("Chuỗi số sau khi xóa các ký tự không phải là số:", so)
    tong_uoc=0
    for i in range(1, so):
        if so%i==0:
            tong_uoc+=i
    if tong_uoc==so:
        print("chuỗi số này là số hoàn hảo")
    else:
        print("chuỗi số này không phải số hoàn hảo")
else:
    print("không có số nào trong chuỗi đã nhập")
