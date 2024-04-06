v_b=input("Nhập đoạn văn bản: ")
trong_v_b=v_b.split()
tu_don=input("Nhập từ đơn: ")
so_lan=0
for tu in trong_v_b:
    if tu.lower()==tu_don.lower():
        so_lan+=1
print("Số lần từ '{}' xuất hiện trong đoạn văn bản là: {}".format(tu_don,so_lan))