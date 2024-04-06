n=int(input("Nhập vào một số nguyên: "))
if n >= 0:
    hang_tram=(n // 100) % 10
    print(f"Chữ số hàng trăm của số đó là :{hang_tram}")
else:
    hang_tram=0
    print(hang_tram)