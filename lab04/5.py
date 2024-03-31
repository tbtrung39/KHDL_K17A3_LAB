cac_so=[]
while True:
    so=int(input("Nhap vao mot so nguyen (nhap so am de dung lai): "))
    if so < 0:
        break
    cac_so.append(so)
print("Cac so ban da nhap la:", cac_so)