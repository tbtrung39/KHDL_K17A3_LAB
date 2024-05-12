def find_dogs_and_chickens(total_legs, quantities, chickens=0):
    if chickens > quantities:
        return [0, 0]

    dogs = quantities - chickens
    chicken_legs = 2
    dog_legs = 4

    if chicken_legs * chickens + dog_legs * dogs == total_legs:
        return [chickens, dogs]
    else:
        return find_dogs_and_chickens(total_legs, quantities, chickens + 1)

quantities = 36
total_legs = 100
final_result = find_dogs_and_chickens(total_legs, quantities)
print(f'Số gà là: {final_result[0]}')
print(f'Số chó là: {final_result[1]}')
