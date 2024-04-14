m= int(input("Nhâph hàng m:"))
n= int(input("Nhập cột n:"))
maTran=[]
for i in range(m):
    hang=[]
    for j in range(n):
        phan_tu= int(input(f'Nhập phần tử hàng {i+1},cột {j+1} vào ma trận: '))
        hang.append(phan_tu)
    maTran.append(hang)
for hang in maTran:
    print(hang)

tong=0
for hang in maTran:
    for phan_tu in hang:
        tong+=phan_tu
print(f"Tổng các phần tử là: {tong}")