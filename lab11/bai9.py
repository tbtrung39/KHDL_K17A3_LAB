
with open("lab11/PASSENGER.IN",mode='r') as file:
    line_1_in_data = file.readline()
    data = file.read().strip().split()
    weight = []
    for numbers in data:
        calc = 0
        calc += int(numbers)
        weight.append(calc)
with open("lab11/WEIGHT.OUT",mode='w') as file:
    for weight_info in data:
        file.write(weight_info)
with open("lab11/CANCELED.OUT",mode='w') as file:
    for cancel_info in data:
        if int(cancel_info) >=23:
            file.write(cancel_info)


for weight_info in data:
    print(weight_info, "là tổng trọng lượng các đồ xách tay của khách")
for cancel_info in data:
    print(cancel_info, "là số thứ tự các khách hàng bị hủy chuyến bay")
