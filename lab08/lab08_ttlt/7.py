def tim_so_nho_nhat(a,b,c):
    return min(a,b,c)
def tim_so_lon_nhat(a,b,c):
    return max(a,b,c)
num1 = int(input("Nhap so nguyen thu nhat: "))
num2 = int(input("Nhap so nguyen thu hai: "))
num3  = int(input("Nhap so nguyen thuba :"))
min_number = tim_so_nho_nhat(num1,num2,num3)
max_number = tim_so_lon_nhat(num1,num2,num3)
print("So lon nhat la:",max_number)
print('So nho nhat la: ', min_number)        