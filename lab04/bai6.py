n = input("Nhập vào một dãy số: ")
ket_qua = ""
while n.isnumeric() == False:
    n = input("Đây không phải là số, vui lòng nhập lại: ")
for i in range(0, len(n)):
    if n[i] == "1":
        ket_qua +="Một "
    elif n[i] == "2":
        ket_qua +="Hai "
    elif n[i] == "3":
        ket_qua +="Ba "
    elif n[i] == "4":
        ket_qua +="Bốn "
    elif n[i] == "5":
        ket_qua +="Năm "
    elif n[i] == "6":
        ket_qua +="Sáu "
    elif n[i] == "7":
        ket_qua +="Bảy "
    elif n[i] == "8":
        ket_qua +="Tám "
    elif n[i] == "9":
        ket_qua +="Chín "
    elif n[i] == "0":
        ket_qua +="Không "                                 
print("Dãy số",n,"đọc là: ",ket_qua)  