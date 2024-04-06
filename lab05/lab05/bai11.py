Str1 = "Khoa, khoa hoc ung dung"
words = Str1.split(" ")
if len(words) == 1:
    words = Str1.split(",") 
for word in words:
    print(word)