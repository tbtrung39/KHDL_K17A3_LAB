def minmax(a,b,c):
    print(f'min=',min(a,b,c))
    print(f'max=',max(a,b,c))
a,b,c=map(int,input('nhập 3 số nguyên cần kiểm tra(các nhau bởi dấu cách): ').split())
minmax(a,b,c)