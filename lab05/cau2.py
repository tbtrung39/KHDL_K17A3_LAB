str = input("nhap chuoi :")
print("so luong ki tu khong pha la so hay la chu tieng anh: ", sum(1 for char in str if not char.isalnum() ))