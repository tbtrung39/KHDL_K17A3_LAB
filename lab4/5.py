n=int(input('nhập số ='))
while True:
    if n>=0:
        print('nhập lại số âm')
        n=int(input('nhập lại='))
        continue
    else:
        print('là số âm')
        break

