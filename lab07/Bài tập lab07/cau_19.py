##a=int(input("Nhập MSV muốn thay đổi từ điển:"))
Dict = {
    "1234": "Nguyễn Văn An",
    "5678": "Trần Thị Ba",
    "9012": "Phạm Thanh Châu",
    "3456": "Hoàng Văn Dương",
    "6789": "Mai Thị Giang",
    "0123": "Vũ Văn Hoàng",
    "8901": "Nguyễn Văn Kiên",
    "1357": "Vũ Thị Linh",
    "2468": "Trương Văn Mạnh",
    "3690": "Hoàng Thị Ngọc",
    "7531": "Vũ Thị Oanh",
    "8520": "Lê Thị Phương",
    "9642": "Võ Văn Quyết",
    "4682": "Đặng Văn Sơn",
    "5702": "Hoàng Thị Thanh Nhã",
    "6803": "Trần Thị Uyên"
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
