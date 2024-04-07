# viết phương trình cho phép nhập từ 1->7 trong tuần . 
# sau đó cho biết thứ tự đã nhập có tên là gì và xuất kết quả ra màn hình
# ví dụ 1: sunday 2: Monday......
ngay = int(input("Nhập ngày:"))
if ngay == 1 :
    print ("1: sunday")
elif ngay == 2:
    print("1: Monday")
elif ngay == 3 :
    print("3: Tuesday")
elif ngay == 4 :
    print("4: Wednesday ")
elif ngay == 5 :
    print("5: Thursday")
elif ngay == 6 :
    print("6: Friday")
elif ngay == 7 :
    print("7: Saturday")
else:
    print("Không có kết quả")
