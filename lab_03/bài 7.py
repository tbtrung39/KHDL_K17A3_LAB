# viết chương trình tính tổng nghịch đảo của n số nguyên đầu tiên
# Ví dụ S=1+1/2+1/3+...+1/n
n =  int(input('nhập vào số nguyên n'))
s=0
i=1
for i in range (1,n+1):
    s+=1/i
print(s)
