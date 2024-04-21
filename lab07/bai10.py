m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n: "))
tong = 0
so_chung = set()
for i in str(m):
    for k in str(n):
        if str(i) == str(k):
            so_chung.add(i)
            break
print("Các chữ số chung của số",m,"và",n,"là:",so_chung)        
for j in (so_chung):
    tong += int(j)        
            
print(tong)            