# Viết chương trình tìm số hoàn hảo nhỏ hơn n(với n được nhập từ bàn phím)
# ví dụ 6 là số hh vì 1+2+3=6 ( shh = tổng của ước)
n = int (input('nhập vào số nguyên dương :'))
for i in range (2,n):
    tong=0
    for j in range(1,i):
        if i%j==0:
            tong+=j
    if tong == i:
        print(i)
       