dictionary = {}
for i in range(1, 101):
    binary_str = bin(i)[2:]
    dictionary[i] = binary_str
print(dictionary)
    