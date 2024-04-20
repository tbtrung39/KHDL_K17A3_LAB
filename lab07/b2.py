danh_sach_so=set()
print("Nhập các số tự nhiên (nhập 'xong' để kết thúc): ")
while True:
    so=input()
    if so.lower()=='xong':
        break
    if so.isdigit() and int (so) >= 0:
        danh_sach_so.add(int(so))
    else:
        print("Chỉ nhập số tự nhiên dương")
print("Tập hợp A: ", danh_sach_so)
           