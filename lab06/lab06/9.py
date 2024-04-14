lst=input("nhap cac phan tu trong danh sach. cach nhau bang dau cach: ").split()
lst=[int(i) for i in lst]
for j in lst:
    assert j%2==0, f"khong phai tat ca cac so trong danh sach la so chan"
print("tat ca cac so trong danh sach la so chan")