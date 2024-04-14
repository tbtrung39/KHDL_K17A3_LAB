list = []
name = input('nhap ten nguoi dung:')
tuoi = int(input('nhap tuoi:'))
diem = int(input('nhap diem so: '))
list.append(
    'ten': ten,
    'tuoi': tuoi,
    'diem': diem
)  
list.sort(key=lambda x: (x[0], x[1], x[2]))
print(list)