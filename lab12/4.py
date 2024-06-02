try:
    with open('lab12/thumuc/vanban.txt','r',encoding='utf-8') as file:
        data = file.read()
        print(data)
except Exception as e:
    print(e)
else: 
    with open('lab12/thumuc/vanban2.txt','w',encoding='utf-8') as file2:
        file2.write(data)