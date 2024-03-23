# nhập vào số nguyên 
# yêu cầu xuất ra chữ số hàng trăm của số đó
# nếu không có thì xuất ra 0
x = int(input("Nhập số nguyên :"))
if x < 100 :
    print("xuất ra 0")
else:
    a = (x//100)%10
    print(" xuất ra chữ số hàng trăm:",a)