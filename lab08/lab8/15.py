def a():
    n=int(input('nhập số gía trị:'))
    l=[]
    for i in range(n):
        a=float(input('nhập số:'))
        l.append(a)
    print(list(map(lambda x: x**2,list(filter(lambda x:x%2!=0 ,l)))))
a()
