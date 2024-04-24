ds=[]
n=int(input("Nhập số lượng phần tử trong Numbers:"))
for i in range(n):
    a=int(input(f"Nhập phần tử thứ {i+1}:"))
    ds.append(a)
A=set(ds)
print("Danh sách các số tự nhiên",ds)
print("Danh sách phần tử A:",A)