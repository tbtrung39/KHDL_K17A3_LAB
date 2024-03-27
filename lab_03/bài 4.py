#Viết chương trình in ra tất cả các số nguyên tố bé hơn hoặc bằng n.
# Chương trình chính
n =  int(input('nhập vào số nguyên dương:'))
# print('số ngto <=n là',n)
for i in range(2,n+1):
    so_nt = True
    for j in range(2,int(i**0.5)+1):
        if i%j ==0:
            so_nt = False
            break
    if so_nt:
        print(i,'là số ngto')
