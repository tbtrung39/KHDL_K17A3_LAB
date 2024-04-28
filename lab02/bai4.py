so = int(input("nhap so: "))
if so < 100:
    print("0")
else:
    hang_tram = (so //100) % 10
    print(f"chu so hang tram cu {so} la: {hang_tram}")