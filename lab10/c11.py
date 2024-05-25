from package import doicoso1 as md
from package import doicoso2 as ad
n = int(input("Nhập số: "))
print(md.he_nhi_phan(n))
print(md.he_bat_phan(n))
print(md.he_thap_luc_phan(n))
string = input("Nhập chuỗi: ")
print(ad.loai_ki_tu(string), "là chuỗi cuối cùng")
binary = input("Nhập số nhị phân: ")
print(ad.he_2_sang_he_10(binary), "là hệ thập phân chuyển từ hệ nhị phân")
octal = input("Nhập số bát phân: ")
print(ad.he_8_sang_he_10(octal), "là hệ thập phân chuyển từ hệ bát phân")
hexa = input("Nhập số thập lục phân: ")
print(ad.he_16_sang_he_10(hexa), "là hệ thập phân được chuyển từ hệ thập lục phân")
