ds_sv = []
tiep_tuc = "y"
while tiep_tuc == "y":
    ma_sv = int(input("Nhập mã sinh viên: "))
    ten_sv = (input("Nhập tên sinh viên: "))
    diem_sv = int(input("Nhập điểm sinh viên: "))
    sinh_vien = dict(ma=ma_sv, ten=ten_sv, diem=diem_sv)
    ds_sv.append(sinh_vien)
    tiep_tuc = input("Bạn có muốn tiếp tục chương trình không? (y/n): ")
print(ds_sv)    
    
