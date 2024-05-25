import giaiPt
a = float(input('Nhập vào hệ số a: '))
b = float(input('Nhập vào hệ số b: '))
c = float(input('Nhập vào hệ số c: '))

if giaiPt.pt_bac_nhat(a,b):
    nghiem=giaiPt.pt_bac_nhat(a,b)
    print(f'Nghiệm của phương trình {a}x + {b} =0 là: {nghiem}')
if giaiPt.pt_bac_hai(a,b,c):
    nghiem = giaiPt.pt_bac_hai(a,b,c)
    if isinstance(nghiem,str):
        print(nghiem)
    else:
        print(f'Nghiệm của phương trình {a}x^2 + {b}x + {c} = 0 là: {nghiem}')
        print(f'x1 = {nghiem[0]}')
        print(f'x2 = {nghiem[1]}')