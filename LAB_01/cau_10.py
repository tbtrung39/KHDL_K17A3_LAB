# viết chương trình nhập vào vận tốc a của 1 xe ô tô đang chạy
# khi ng lái đạp phanh ,tính thgian ô tô đi được tới lúc dừng 
#làm tròn đến số thập phân thứ 2
# biết vận tốc chậm dần đều là v(t) = -t.log4(5) + a^4
import math
a=int(input('Nhap vao van toc a mot o to dang chay: '))
t=a**4/math.log(5,4)
print(f'Thoi gian o to di duoc cho den luc dung la {t}')