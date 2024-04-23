thong_tin = {
    "001": ["Nguyễn Văn A", 10],
    "002": ["Trần Thị B", 7.5],
    "003": ["Hoàng Thị C", 7],
    "004": ["Lê Văn D", 9],
    "005": ["Nguyễn Văn E", 8]
}
sbd = input("Nhập số báo danh: ") 
found = False  
for key, value in thong_tin.items():
    if key == sbd:
        found = True
        print(value)  
        break
if not found:
    print("Số báo danh không tồn tại. Bổ sung thông tin cho thí sinh")
    ten = input("Nhập tên học sinh: ")
    diem = float(input("Nhập điểm: "))
    thong_tin[sbd] = [ten, diem]  
    print("Thông tin mới đã được thêm vào từ điển.")
    print(thong_tin)  
