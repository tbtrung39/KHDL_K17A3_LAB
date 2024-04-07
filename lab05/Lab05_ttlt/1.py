str = input("Nhap vao mot chuoi ky tu: ")
print('Chuoi ky tu vua nhap: ', str)
dem = 0
for c in str:
    if "0" <=c <= "9":
        dem+=1
print("Cac ky tu trong chuoi da nhap la: ", dem)
        
