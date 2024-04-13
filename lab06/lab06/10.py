import random
so=[x for x in range(201) if x%5==0 and x&7==0]
random_=random.choice(so)
print(f'Số ngẫu nhiên chia hết cho 5 và 7 từ 0 đến 200: {random_}')