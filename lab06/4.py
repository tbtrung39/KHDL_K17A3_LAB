danh_sach=[]
while True:
    n=int(input("Nhập số tự nhiên n: "))
    if n<=0:
        break
    danh_sach.append(n)
print("Danh sách sau khi nhập: ",danh_sach)

#Sắp xếp danh sách
danh_sach.sort()
print(danh_sach)

danh_sach.sort(reverse=True)
print(danh_sach)

#Chèn phần tử vào danh sách
danh_sach.append([1,2,3])
print("Danh sách sau khi đã chèn thêm phần tử: ",danh_sach)

danh_sach.insert(0,[1,2,3])
print(danh_sach)

danh_sach.insert(4,[1,2,3])

print(danh_sach)

#Xóa phần tử khỏi danh sách
k=int(input("Nhập vị trí phần tử cần xóa: "))
danh_sach.pop(k)
print("Danh sách sau khi xóa: ",danh_sach)

