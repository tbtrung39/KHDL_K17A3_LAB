str1 = 'khoa , khoa hoc ung dung'
split = str1.split(" ")
split = [word.strip(',') for word in split]
for word in split:
    print(word)