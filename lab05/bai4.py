str_1 = input("Nhập vào chuỗi 1: ")
str_2 = input("Nhập vào chuỗi 2: ")
tron_chuoi = ""
i = 0
while i < len(str_1) or i < len(str_2):
    if i < len(str_1):
        tron_chuoi += str_1[i]
    if i < len(str_2):
        tron_chuoi += str_2[i]
    i+=1    
print("Chuỗi được trộn từ",str_1,"và",str_2,"là:",tron_chuoi)    