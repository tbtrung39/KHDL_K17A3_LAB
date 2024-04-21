m=set(str(int(input())))
n=set(str(int(input())))
q=m.intersection(n)
result=0
for i in q:
    result+=int(i)
print(result)