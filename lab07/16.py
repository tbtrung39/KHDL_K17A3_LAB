a=[]

while True:
     b=input('nhập số(a để thoát):')
     if b=='a':
         break
     a.append(int(b))
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i]+1==a[j] and i<j:
            print(f'({i},{j})')