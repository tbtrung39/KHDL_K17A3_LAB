so = int(input("Nhập số nguyên 3 chữ số: "))
hang_tram = 0
if so >=100:
  hang_tram = (so//100)%10
print("Chữ số hàng trăm là: ", hang_tram)