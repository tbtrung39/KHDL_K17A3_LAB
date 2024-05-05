str = input('Nhap chuoi: ')
 # khoi tao bien dem so chu cai
so = 0
# duyet tung ky tu cua chuoi
for char in str:
    if  not char.isalpha() and not char.isdigit():
        so +=1
print("Ky tu khong phai la chu cai Tieng Anh va khong co trong chuoi la: ", so)
        