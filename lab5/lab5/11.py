Str1 = "Ngoc Huyen, một ngừi tốt bụng và tuỵt zời"

tu = Str1.split(' ') 
tu = [word.strip(',') for word in tu] 

for word in tu:
    print(word)