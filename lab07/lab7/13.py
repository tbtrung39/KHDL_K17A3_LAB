W = input("Nhập chuỗi W: ")
dictionary = {}
length = len(W)
for i in range(length):
    for j in range(i+1, length+1):
        sub_string = W[i:j]
        if sub_string in dictionary:
            dictionary[sub_string] += 1
        else:
            dictionary[sub_string] = 1
print(dictionary)