ds=[]
n=int(input("Nhập số lượng phần tử muốn nhập vào danh sách:"))
for i in range(n):
    a=int(input(f"Nhập phần tử thứ {i+1}:"))
    ds.append(a)
so_tiep=0
num=2
for j in ds:
    if j%j == 0:
        num+=j
print(ds)