ds=[]
n=int(input("Nhập số lượng phần tử trong tập hợp A:"))
for i in range(n):
    a=int(input(f"Nhập phần tử thứ {i+1}:"))
    ds.append(a)
print(f"Phần tử lớn nhất trong danh sách:{max(ds)}")
print(f"Phần tử nhỏ nhất trong danh sách:{min(ds)}")

#tổng
tong=0
for i in ds:
    tong+=i
print("Tổng các phần tử trong danh sách là ",tong)