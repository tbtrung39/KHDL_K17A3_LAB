# Viet chuong trinh hap vao su dung lenh assert de xac minh tat ca cac so trong mot list da nhap
list =[int(n) for n in input("Nhap danh sach cac so , cach nhau boi dau cach:").split()]
for m in list:
    assert m % 2 == 0
    print(f' So {m} khong phai la so chan')
print("Tat ca cac so trong danh sach deu la so chan")
