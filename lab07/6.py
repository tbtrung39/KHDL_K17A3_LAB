n = int(input('nhập vào số tự nhiên n: '))
a=[]
num=2
while len(a)<n:
    is_a = True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_a = False 
            break
    if is_a:
        a.append(num)
    num+=1
print(a)