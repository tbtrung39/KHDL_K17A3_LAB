Str=input('nhập chuỗi kí tự:')
b=''.join(filter(str.isdigit,Str))
print('chuỗi số sau khi loại bỏ các khí tự không phải số là:',b)
c=int(b)
k=0
for i in range(1,c):
    if c%i==0:
        k+=1
if k ==c:
    print('là số hoàn hảo')
else:
    print('không phải số hoàn hảo')