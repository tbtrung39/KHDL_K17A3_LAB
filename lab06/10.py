import random
numbers=[x for x in range(201) if x%5==0 and x&7==0]
random_number=random.choice(numbers)
print("Số ngẫu nhiên chia hết cho 5 và 7 từ 0 đến 200:", random_number)