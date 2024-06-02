a=set()
while True:
    n=input('nhập kí tự (ESC kết thúc): ')
    if n.upper()=='ESC':
        break
    if not n.isdigit():
        a.add(n)
print(f'tập hợp sau khi xóa các ký tự số: {a}')