a=[]
while True:
    name=input('name: ')
    age=int(input('age: '))
    score=float(input('score: '))
    a.append((name,age,score))
    tt = input('tiếp tục(y/n): ').strip().lower()
    if tt == "n":
        break
sorted_list = sorted(a,key=lambda x: (x[0], x[1], x[2]))
for i in sorted_list:
    print(i)