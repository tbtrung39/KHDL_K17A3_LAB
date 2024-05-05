# Viết chương trình tạo 1 list chứa toàn số chẵn thuộc khoảng [1..100]
def so_chan():
    list_so_chan = []
    for i in range(1,101):
        if i % 2 == 0:
            list_so_chan.append(i) 
    return list_so_chan

print("List chứa toàn số chẵn thuộc khoảng [1..100] là:", so_chan())
