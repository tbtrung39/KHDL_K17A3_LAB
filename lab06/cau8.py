n=int(input('nhập n: '))
fibo=[0,1]
[fibo.append(fibo[-1]+fibo[-2]) for i in range(2,n)]
print(fibo)