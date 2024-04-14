import random
a=[['mon', 73], ['tue', 89], ['wed', 95], ['thu', 103], ['fri', 115], ['sat', 128], ['sun', 120]]
print(f'Danh sách a: {a}')
phan_tu=a[2][1]
print("Phần tử thứ hai thuộc ví trí thứ 3 của sublist:", phan_tu)
a.append(["new_day", random.randint(50, 200)])
print(f'a sau khi thêm một sublist ngẫu nhiên {a}')
tinh_toan=['tue', 'wed', 'sat', 'sat', 'sun']
s =sum(sublist[1] for sublist in a if sublist[0] in tinh_toan)
print(f'Tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật: {s}' )