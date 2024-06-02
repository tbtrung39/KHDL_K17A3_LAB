def c(a,b):
    m=max(a,b)
    for i in range(m,0,-1):
        if a%i==0 and b%i==0:
            return i
        
a=int(input('nhập tử số:'))
b=int(input('nhập mẫu số:'))
if __name__=='__main__':
    print(f'UCLN:{c(a,b)}')
    print(f'phân số sau khi rút gọn:{int(a/c(a,b))}/{int(b/c(a,b))}')
            
        
    