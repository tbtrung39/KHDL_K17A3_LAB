n=input('nhập: ')
k=0
for i in n:
    if not i.isalpha() and not i.isdigit():
        k+=1
print('so kí tu không phải chữ cái tiếng anh và sô là',k)