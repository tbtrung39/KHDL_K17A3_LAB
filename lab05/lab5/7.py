Str = input("Nhập đoạn văn bản: ")
word = input("Nhập từ đơn: ")

words = Str.split()

count = words.count(word)

print("Từ đơn '{}' xuất hiện {} lần trong đoạn văn.".format(word, count))
