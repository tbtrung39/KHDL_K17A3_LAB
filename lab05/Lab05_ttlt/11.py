str = input("Nhap mot chuoi ky tu nhi phan: ")
so_thap_phan = 0
for i in range(len(str)):
    so_thap_phan += int(str[i]) + (2**(len(str) - 1 - i))
print(f"so thap phan tuong ung la: ",so_thap_phan)    