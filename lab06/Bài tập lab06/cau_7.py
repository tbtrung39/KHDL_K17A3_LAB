List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
for i in List_:
    print("Các phần tử của ", i)
#   
phan_tu = List_[1][1]
print(phan_tu)
# 
print(len(List_))
List_.append(["nine", 119])
# 
tong_sale = 0
for i in List_:
    if i[0] == "mon" or i[0] == "tue" or i[0] == "sat" or i[0] == "sun":
        tong_sale += i[1]
print("Tổng sale các ngày thứ 2, 3, 7 và chủ nhật là: ", tong_sale)
