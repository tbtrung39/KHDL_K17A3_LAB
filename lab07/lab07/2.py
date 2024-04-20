numbers=[]
while True:
    n=input(' nhập giá trị :')
    if n=='esc':
        break
    numbers.append(n)
a=set(numbers)
print('tập hợp A là :',a)