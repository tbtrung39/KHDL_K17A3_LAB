import random
List_=[["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách List_:", List_)
phan_tu=List_[2][1]
print("Phần tử thứ hai thuộc ví trí thứ 3 của sublist:", phan_tu)
List_.append(["new_day", random.randint(50, 200)])
print("List_ sau khi thêm một sublist ngẫu nhiên:", List_)
ngay_tinh_toan=["tue", "wed", "sat", "sat", "sun"]
tong_sale_value=sum(sublist[1] for sublist in List_ if sublist[0] in ngay_tinh_toan)
print("Tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", tong_sale_value)