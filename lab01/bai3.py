r = int(input("Nhập bán kính hình trụ: "))
h = int(input("Nhập chiều cao hình trụ: "))
s_xq = 2*3.14*r*h
s_tp = 2*3.14*r*(r+h)
v = 3.14*(r**2)*h
print("Diện tích xung quanh hình trụ là: ",s_xq)
print("Diện tích toàn phần hình trụ là: ",s_tp)
print("Thể tích khối trụ là: ",v)