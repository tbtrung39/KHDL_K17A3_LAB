so = int(input("Nhap vao mot so nguyen: "))
chu_so_hang_tram = (so // 100) % 10
if chu_so_hang_tram !=0:
    print("chu so hang tram cua so do la", chu_so_hang_tram)
else:
    print("xuat ra 0")