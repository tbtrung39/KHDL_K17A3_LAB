n=int(input("Nhập số lượng phần tử của list: "))
list_so_nguyen=[]
for i in range(n):
    so_nguyen=int(input(f"Nhập phần tử thứ {i+1}: "))
    list_so_nguyen.append(so_nguyen)
list_binh_phuong_le=list(map(lambda x: x**2, filter(lambda x: x%2!=0, list_so_nguyen)))
print("List ban đầu:", list_so_nguyen)
print("List chứa bình phương của các số lẻ trong list ban đầu:", list_binh_phuong_le)