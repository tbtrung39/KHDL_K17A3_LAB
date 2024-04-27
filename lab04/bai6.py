while True:
    n = int(input("Nhap so can tim"))
    if n<0:
        print("So can tim khong hop le")
    else:
     dayso=str(n)
     socantim = {
    '0': 'không',
    '1': 'một',
    '2': 'hai',
    '3': 'ba',
    '4': 'bốn',
    '5': 'năm',
    '6': 'sáu',
    '7': 'bảy',
    '8': 'tám',
    '9': 'chín'
}
     for i in dayso:
      print(socantim[i])