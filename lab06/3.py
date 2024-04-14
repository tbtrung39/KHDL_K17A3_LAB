danh_sach=[]
while True:
    n=int(input("Nhập số tự nhiên n: "))
    if n<=0:
        break
    danh_sach.append(n)
print("Danh sách sau khi nhập: ",danh_sach)


m=int(input("Nhập m để thêm vào cuối danh sách: "))
danh_sach.append(m)
print("Danh sách sau khi thêm m: ",danh_sach)

danh_sach.insert(4,m)
print("Danh sách sau khi thêm m: ",danh_sach)