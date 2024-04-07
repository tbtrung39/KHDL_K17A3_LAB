chuoi = input("Nhập vào một chuỗi: ")
ki_tu = chuoi[0]
chuoi_con = ""
ket_qua = ""
for c in chuoi:
    print("c = ", c)
    if c == ki_tu:
        chuoi_con = chuoi_con + c
    else:
        
        if len(chuoi_con)>len(ket_qua):
            ket_qua = chuoi_con
        chuoi_con = c
        ki_tu = c
    print("ki tu = ", ki_tu)
    print("chuoi_con = ", chuoi_con)
    print("ket qua = ", ket_qua)
    
if len(chuoi_con)>len(ket_qua):
    ket_qua = chuoi_con
    
print(ket_qua)
            