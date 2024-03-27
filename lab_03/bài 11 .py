# viết chương trình nhập một số làm số hàng của tam giác với độ rỗng nhv
#c
n=int(input('nhập giá trị chiều cao cuar tam giác:'))
k=2*n-2   # xác định khoảng trắng
for dong in range(1,n+1):
    for cot in range(1,k+1):
        print(end=' ')
    for cot in range(1,dong+1):
        print('*',end=' ')
    k=k-1
    print('\r')
n=int(input('nhập giá trị chiều cao cuar tam giác:'))
k=2*n-2   # xác định khoảng trắng
for dong in range(1,n+1):
    for cot in range(1,k+1):
        print(end=' ')
    for cot in range(1,dong+1):
        print('*',end=' ')
    k=k-1
    print('\r')
