a=[]
def thong_tin(a):
    ten=input('nhập họ và tên: ')
    toan=float(input('nhập điểm toán: '))
    ly=float(input('nhập điểm lý: '))
    hoa=float(input('nhập điểm hóa: '))    
    a.extend([ten,toan,ly,hoa])
def xuat(a):
    print('thông tin đã nhập:')
    print(f'họ và tên: {a[0]}')
    print(f'điểm toán: {a[1]}')
    print(f'điểm lý: {a[2]}')
    print(f'điểm hóa: {a[3]}')
def tb(a):
    tb=sum(a[1::])
    print(f'điểm trung bình là: {tb}')
thong_tin(a)
xuat(a)
tb(a)