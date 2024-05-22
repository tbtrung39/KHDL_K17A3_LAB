import package_1
a = int(input("Nhập độ dài cạnh a: "))
b = int(input("Nhập độ dài cạnh b: "))
c = int(input("Nhập độ dài cạnh c: "))
print()
if package_1.my_Triange.kiem_tra_tam_giac(a,b,c):
    print("Ba cạnh này tạo thành một tam giác")
    chu_vi = package_1.my_Triange.chu_vi_tam_giac(a,b,c)
    print("Chu vi của tam giác bằng:",chu_vi)
    dien_tich = package_1.my_Triange.dien_tich_tam_giac(a,b,c)
    print("Diện tích của tam giác bằng:",dien_tich)
else:
    print("Đây không phải là tam giác")    
