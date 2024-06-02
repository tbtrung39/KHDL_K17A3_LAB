def thongtin(d:dict):
    hoten=input('nhập họ tên:')
    que=input('nhập quê quán:')
    tnien=float(input('nhập thâm niên công tác:'))
    d['họ tên']=hoten
    d['quê quán']=que
    d['thâm niên công tác']=tnien
    return d

def luong(a):
    if a<12:
        b=2.34
    elif a>=12 and a<36:
        b=3.33
    elif a>=36 and a<60:
        b=3.66
    else:
        b=3.99
    c=b*1350000
    return c

def xuat(d:dict):
    d['lương']=luong(d['thâm niên công tác'])
    return d

def main():
    a=dict()
    print('thông tin đã nhập:',thongtin(a))
    print(xuat(a))

main()