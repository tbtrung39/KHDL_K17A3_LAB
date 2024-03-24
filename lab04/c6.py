n = input("Nhập dãy số: ")
while n =="0":
    break
ket_qua = ""
for i in range(len(n)):
    if n[i] =='1':
        ket_qua += "Một "
    if n[i] =='2':
        ket_qua += "Hai "
    if n[i] =='3':
        ket_qua += "Ba "
    if n[i] =='4':
        ket_qua += "Bốn "
    if n[i] =='5':
        ket_qua += "Năm "
    if  n[i] =='6':
        ket_qua += "Sáu "
    if n[i] =='7':
        ket_qua += "Bảy "
    if n[i] =='8':
        ket_qua += "Tám "
    if n[i] =='9':
        ket_qua += "Chín "
    if n[i] =='0':
        ket_qua += "Không "
print("Dãy số ", n, "đọc là: ", ket_qua)

    
    
        

