W=input("Nhập chuỗi ký tự: ")
dictionary={ }
for i in range(len(W)):
    for j in range(i+1, len(W)+1):
        sub_string=W[i:j]
        if sub_string in dictionary:
            dictionary[sub_string]+=1
        else:
            dictionary[sub_string]=1
print("Từ diển có các cặp (K, V): ", dictionary)