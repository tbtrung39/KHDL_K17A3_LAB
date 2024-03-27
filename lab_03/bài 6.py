# viết chương trình tính tổng bậc 3 của n số nguyên đầu tiên.In kq ra màn hình
n =  int(input('nhập vào số nguyên n:'))
s=0
i=1
for i  in range (1,n+1):
    s+=i**3
print(s)