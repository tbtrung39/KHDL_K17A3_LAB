so = int(input("Nhập vào một số nguyên dương: "))
tong = 0
while so<0:
    so = int(input("Số",so,"không phải là số nguyên dương, vui lòng nhập lại: "))
so_copy = so
while so>0:
    tong+=so%10
    so=so//10   
print("Tổng của số",so_copy,"là: ",tong)