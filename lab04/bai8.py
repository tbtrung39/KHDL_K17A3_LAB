while True:
    list= {
    "1":"Cafe",
    "2":"Cam vắt",
    '3':'Nước ép cà rốt',
    "4":"Nước lọc",
    "5":"Nước dừa",
    }
    n = int(input("Vui long chon do uong ( Nhap so tu 1 den 5)"))
    douong = str(n)
    if n>=6:
       print("Vui long nhap lai lua chon cua ban")
    else:
     for i in douong:
      print("Bạn đã chọn",list[i])
      break