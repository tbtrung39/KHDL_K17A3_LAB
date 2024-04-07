# tim bcnn cua hai so nguyen duoc nhap tu ban phim
so_1= int(input('Nhap so thu nhat: '))
so_2 = int(input("Nhap so thu hai: "))
#tim ucln 
a,b = so_1,so_2
while b!=0:
    a,b = b,a % b
# tinh bcnn
boi_chung = (so_1 * so_2) // a

print("Bcnn cua: ", so_1, "va",so_2, "la:", boi_chung)
        