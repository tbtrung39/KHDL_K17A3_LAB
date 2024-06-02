##a=int(input("Nhập MSV muốn thay đổi từ điển:"))
Dict = {
    "1234": "Nguyễn Văn A",
    "5678": "Trần Thị B",
    "9012": "Phạm Thanh C",
    "3456": "Hoàng Văn D",
    "7890": "Lê Thị E",
    "2345": "Đỗ Văn F",
    "6789": "Mai Thị G",
    "0123": "Vũ Văn H",
    "4567": "Lý Thị I",
    "8901": "Ngô Văn K",
    "1357": "Bùi Thị L",
    "2468": "Trương Văn M",
    "3690": "Dương Thị N",
    "7531": "Quách Văn O",
    "8520": "Lưu Thị P",
    "9642": "Võ Văn Q",
    "3579": "Tạ Thị R",
    "4682": "Đặng Văn S",
    "5702": "Hoàng Thị T",
    "6803": "Trần Văn U"
}
newDict=[]
while True:
    a=input('Nhập lựa chọn :')
    print('1,Tạo mới từ điển')
    if a == '1':
        MSV=input("Nhập MSV muốn tạo mới:")
        tenSV=input("Nhập tên sinh viên muốn tạo mới:")
        newDict[MSV]=tenSV
        print(newDict)
    elif a == '2':
        sl=int(input('Nhập số lượng sinh viên muốn thêm vào danh sách:'))
        for i in range(sl):
            MSV1=int(input(f"Nhập MSV thứ {i+1}:"))
            tenSV1=input(f"Nhập tên SV thứ {i+1} :")
            newDict.append({MSV1,tenSV1})
        print(newDict)
    else:
        print("0,Thoát chương trình")
        break

