a=dict()
while True:
    b=input('nhập mã sinh viên gồm 6 chữ số:')
    if len(b)!=6 and not(b.isnumeric()):
        print('vui lòng nhập lại MSV')    
        continue
    else:
        c=input('nhập tên sinh viên:')
        d=float(input('nhập điểm:'))
        if not(0<=d<=10):
            print('nhập lại điểm số trong khoảng 0->10')
            continue
        a[b]=[c,round(d,0)]
    e=input('tiếp tục nhập?(y or n):')
    if e=='n':
        break
dic=dict(sorted(a.items(),key=lambda item:item[1][1],reverse=True))
print(dic)