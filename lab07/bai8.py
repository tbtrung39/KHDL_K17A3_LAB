import random
A = [] 
for i in range(10):
    rand_choice = random.choice([1,2,3]) 
    if rand_choice == 1:
        A.append(random.randint(-100, 100)) 
    elif rand_choice == 2:
        A.append(random.uniform(-100, 100)) 
    else:
        A.append(''.join(random.choices('abcdef', k=5))) 

int_count= sum(isinstance(x, int)for x in A)
float_count = sum(isinstance(x, float)for x in A)
str_count = sum(isinstance(x, str) for x in A)

print("Tập hợp A là :", A)
print("số phần tử là số nguyên trong tập hợp A là: ",int_count)
print("số phần tử là số thực trong tập hợp A là:",float_count)
print("số phần tử là chuỗi ký tự trong tập hợp A là:",str_count)