#1
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print(List_)
#2
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print(List_[2])
#3
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
len(List_)
print("Do dai cua list la :", len(List_))
List_.append(["New day", 200])
print("Danh sach duoc them vao la", List_)
#4
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
Tong_sale_value = List_[0][1] + List_[1][1] + List_[5][1] + List_[6][1]
print("Tong sale value trong ngay thu 2,3,7, chu nhat la :", Tong_sale_value)