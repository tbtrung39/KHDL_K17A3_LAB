tnct=int(input('nhap tham niem cong tac: '))
if tnct<12:
    hs=2.34
elif 12<=tnct<36:
    hs=3.33
elif 36<=tnct<60:
    hs=3.66
elif tnct>60:
    hs=3.99
print(f'luong cua nhan vien la:{hs*1350000} dong')
