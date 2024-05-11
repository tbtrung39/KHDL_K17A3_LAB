quantities = 36
total_legs = 100
def find_dogs_and_chickens(total_legs, quantities):
    chicken_legs = 2
    if total_legs ==0:
        return [0,0]
    elif total_legs % 2 !=0:
        return [0,0]
    elif chicken_legs * quantities == total_legs:   
        return [quantities,0]
    for chickens in range(0,quantities +1):
        dogs = quantities - chickens
        result = find_dogs_and_chickens(total_legs - chicken_legs, quantities -1)
        if result[0] + dogs == quantities and result[1] + chickens == quantities:
            return [chickens,dogs]
    return [0,0]

final_result = find_dogs_and_chickens(total_legs,quantities)
print("Số gà là: ", final_result[0])
print("Số chó là: ", final_result[1])