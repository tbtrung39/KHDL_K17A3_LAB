#1
danh_sach_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print(danh_sach_)
#2
danh_sach_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print(danh_sach_[2])
#3
danh_sach_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
len(danh_sach_)
print("Do dai cua danh_sach la :", len(danh_sach_))
danh_sach_.append(["New day", 200])
print("Danh sach duoc them vao la", danh_sach_)
#4
danh_sach_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
Tong_sale_value = danh_sach_[0][1] + danh_sach_[1][1] + danh_sach_[5][1] + danh_sach_[6][1]
print("Tong sale value trong ngay thu 2,3,7, chu nhat la :", Tong_sale_value)