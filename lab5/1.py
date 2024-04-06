str = input('nhập chuỗi kí tự :')
print('chuỗi kí tự vừa nhập',str)
d=0
for c in str:
    if '0'<=c<='9':
        d+=1
print('số kí tự đa nhập',d)
