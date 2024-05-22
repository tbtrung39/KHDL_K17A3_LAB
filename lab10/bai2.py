import package_2
n = int(input("Nhập độ dài cạnh hình vuông: "))
while n < 0:
    n = int(input("Độ dài không hợp lệ, hãy nhập lại: "))
chu_vi = package_2.my_square.chu_vi_hinh_vuong(n)
print("Chu vi hình vuông là:",chu_vi)
dien_tich = package_2.my_square.dien_tich_hinh_vuong(n)
print("Diện tích hình vuông là:",dien_tich)