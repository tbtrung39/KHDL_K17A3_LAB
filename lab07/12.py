n=int(input('nhập dữ liệu:'))
dic={}
for i in range(1,n+1):
    dic[f'{i}']=i**2
print(dic)