def hoan_vi(n,i):
    if i==len(n)-1:
        print(n)
    else:
      for j in range(i,len(n)):
        n[i],n[j]=n[j],n[i]
        hoan_vi(n,i+1)  
        n[i],n[j]=n[j],n[i]
a=int(input('nhập phần tử tự nhiên:'))
danh_sach=list(range(1,a+1))
hoan_vi(danh_sach,0)
