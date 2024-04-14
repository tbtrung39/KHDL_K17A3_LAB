n=int(input('nhập n: '))
fibonaci=[0,1]
[fibonaci.append(fibonaci[-1]+fibonaci[-2]) for i in range(2,n)]
print(fibonaci)