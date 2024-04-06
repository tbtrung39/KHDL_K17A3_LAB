a = input('Nhập vào một chuỗi kí tự: ')
cso = ''.join(filter(str.isdigit,a))
print(f'Chuỗi số sau khi xóa không phải là số: {cso}')

if cso.isdigit():
    so = int(cso)
    tong = 0
    for i in range(1,so):
        if so%i==0:
            tong+=1
    if tong == so:
        print(f'Chuỗi này là số hoàn hảo.')
    else:
        print(f'Chuỗi này không phải là số hoàn hảo.')
else:
    print(f'Chuỗi này không phải là số.')