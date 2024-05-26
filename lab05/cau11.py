isNhiPhan = False
while isNhiPhan == False:
    nhi_phan = input("Nhập vào một chuỗi nhị phân: ")
    for i in nhi_phan:
        if i not in ["0","1"]:
            isNhiPhan = False
            print("Đây không phải là chuỗi nhị phân")
            break
        else:
            isNhiPhan = True
    
print("Chuỗi nhị phân vừa nhập là: ",nhi_phan)
thap_phan = 0
for i in range (len(nhi_phan)):
    thap_phan += int(nhi_phan[i]) * (2**(len(nhi_phan)-1-i))
print("Dãy số nhị phân",nhi_phan,"chuyển sang số thập phân là: ",thap_phan)