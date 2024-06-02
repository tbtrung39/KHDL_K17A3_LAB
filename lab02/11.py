ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
if ngay <1 or ngay >31:
    print("Tháng",thang."Không có ngày",ngay)
elif thang <1 or thang >12:
    print("Không có tháng",thang)
elif thang ==2:
    if ngay >29:
        print("Tháng 2 không có ngày",ngay)
    elif ngay == 29:
        print("Ngày tiếp theo là ngày 1 tháng", thang+1)
    else:    
        print("Ngày tiếp theo là ngày",ngay+1,"tháng",thang)    
elif thang in [4,6,9,11]:
    if ngay >30:
        print("Tháng",thang,"không có ngày",ngay)
    elif ngay == 30:    
        print("Ngày tiếp theo là ngày 1 tháng",thang+1)
    else:
        print("Ngày tiếp theo là ngày",ngay+1,"tháng",thang)
else:
    if ngay == 31:
        print("Ngày tiếp theo là ngày 1 tháng",thang+1)
    else:
        print("Ngày tiếp theo là ngày",ngay+1,"tháng",thang)   