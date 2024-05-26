str = input ("nhap vao  mot chuoi ky tu : ")
print("chuoi ky tu vua nhap ",str)
dem = 0
for c in str:
    if "0"<=c<="9":
        dem +=1
        print("so cac ky tu la so trong chuoi da nhap= ", dem)