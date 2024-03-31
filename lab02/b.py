# viết chương trình in ra màn hình học lực cử học sinh
# điểm từ 0.0 -> 3.0 : loại kém
# điểm từ 4.0 : loại yếu
# điểm từ 5.0 -> 6.0 : loại trung bình
# điểm từ 7.0 -> 8.0 : loại khá
# điểm từ 9.0 -> 10.0 : loại giỏi
diem = float(input("yêu cầu nhập điểm:"))
if diem < = 3:
    print(" loại kém")
elif diem == 4:
    print(" loại yếu")
elif diem <= 6 :
    print(" loại trung bình")               # lỗ hổng nhập 11 vẫn ra loại giỏi không hợp lệ
elif diem <= 8 :
    print("loại khá")
else:
    print(" loại giỏi")


# cách khác :
if diem >=0 and diem <= 3 :
    print("loại kém")
if diem == 4:
    print("loại yếu")
if diem >=5 and diem <=6 :
    print(" loại trung bình") 
if diem >=7 and diem <=8 :
    print(" loại khá")
if diem >=9 and diem <= 10 :
    print(" loại giỏi")                           


# phương trình đường tòn có dạng
#(x-a)^2  + (y-b)^2 = r^2
# va diem M(c,d) bat ky
# nhap tu ban phim a,b,c,d va r
# xác định ví trí của M với đường tròn

a = int(input(" nhập a:"))
b = int(input(" nhập b:"))
c = int(input(" nhập c:"))
d = int(input(" nhập d :"))
r = int(input(" nhập r:"))
# I(a,b)
# M(c,d)
# R = r
khoang_cach_IM =((a-c)**2 + (b-d)**2)**0.5
if khoang_cach_IM > r:
    print(" M nằm ngoài đường tròn")
elif khoang_cach_IM < r :
    print(" M nằm trong đường tròn")
else:
    print(" M nằm trên đường tròn")