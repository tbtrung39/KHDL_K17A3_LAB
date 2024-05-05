a=list(input('nhập danh sách các số:'))
b=list(input('nhập danh sách tên:'))
dic={}
min=min(len(a),len(b))
for i in range(0,min):
    dic[a[i]]=b[i]
print(dic)