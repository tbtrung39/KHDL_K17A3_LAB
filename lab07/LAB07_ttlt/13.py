w =input("Nhap chuoi ky tu: ")
dictionary = {}
for i in range(len(w)):
    for j in range(i+1, len(w)+1):
        substring = w[i:j]
        if substring in  dictionary:
            dictionary[substring] +=1
        else:
            dictionary[substring] =1
print(dictionary)                