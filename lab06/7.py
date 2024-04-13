
List_=[["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
for i in List_:
    print(i)

element=List_[1][1]
print(element)

a=len(List_)
print(a)
List_.append(['one',111])

tong=0
for i in List_:
    if i[0]=='mon' or i[0]=='tue' or i[0]=='sat' or i[0]=='sun':
        tong+=i[1]
print('tong sale value trong thu 2, 3,7,8 là: ',tong)