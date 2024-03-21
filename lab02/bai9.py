so_kw =int(input("nhap so kw dien:"))
if so_kw <0:
    so_kw = int(input("nhap so kw dien:"))
else:
    if so_kw >=0 and so_kw<=100:
        don_gia=2000*so_kw
    elif so_kw>=  101 and so_kw<=200:
        don_gia= (2000*100)+((so_kw - 100) * 2500)
    elif so_kw >=201 and so_kw <=300:
        don_gia = (2000*100)+(100 * 2500)+((so_kw -200)*3000)
    elif so_kw >300:
        don_gia = (2000*100)+(100 * 2500)+(100*3000)+((so_kw-300)*5000)
    print("so tien phai tra :", don_gia)