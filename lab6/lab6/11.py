A=list(map(int,input('nhập danh sach A, cách nhau bơi dấu cách: ').split()))
B=[i for i in A if i % 3==0 and i % 5 !=0]
print(f'danh sach B: {B}')
C=[i**2 for i in A]
print(f'danh sach C: {C}')
D=[i for i in A if i%3==0]
print(f'danh sach D: {D}')