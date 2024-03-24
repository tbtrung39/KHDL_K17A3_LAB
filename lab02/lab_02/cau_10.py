# một điểm cho thuê sân tập bóng theo công thức:
# mỗi giờ trong 03 giờ đầu tiên tính 100000đ/giờ
# mỗi giờ ttheo giảm 25% so vs đơn giá trong 3 giờ đầu tiên
# ngoài ra nếu tgian thuê từ 11-> 15h đc giảm 10%
# vt chương trình nhập vào giờ bắt đầu,giờ kết thúc và in ra số tiền khách thuê sân phải trả
# biết rằng 5h <= giờ bắt đầu <= giờ kết thúc <= 22
start=int(input('nhập giờ bắt đầu(5->22):'))
end=int(input('nhập giờ kết thúc(5->22):'))
thoi_gian=end-start 
if thoi_gian<=3:
    tien=thoi_gian*100000
else:
    tien=thoi_gian*100000*(3/4)
if 11<=start<=14 and 12<=end<=15:
    tien=tien*(9/10)
print(f'tiền phải trả:{tien}')