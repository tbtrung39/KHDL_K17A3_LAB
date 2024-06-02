def check_passengers(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        num_passengers = int(lines[0])
        passenger_weights = [sum(map(int, line.split())) for line in lines[1:]]

        overweight_passengers = [i+1 for i, weight in enumerate(passenger_weights) if weight > 23]
        excessive_items_passengers = [i+1 for i, items in enumerate(lines[1:]) if len(items.split()) > 5]

        return num_passengers, passenger_weights, overweight_passengers, excessive_items_passengers

def write_output(weight_output_file, canceled_output_file, num_passengers, passenger_weights, overweight_passengers, excessive_items_passengers):
    with open(weight_output_file, 'w') as weight_file:
        for weight in passenger_weights:
            weight_file.write(str(weight) + '\n')

    with open(canceled_output_file, 'w') as canceled_file:
        canceled_passengers = set(overweight_passengers + excessive_items_passengers)
        for passenger in canceled_passengers:
            canceled_file.write(str(passenger) + '\n')

# Đường dẫn tới các file dữ liệu
input_file = 'PASSENGERS.IN'
weight_output_file = 'WEIGHT.OUT'
canceled_output_file = 'CANCELED.OUT'

# Kiểm tra hành khách và viết kết quả ra file
num_passengers, passenger_weights, overweight_passengers, excessive_items_passengers = check_passengers(input_file)
write_output(weight_output_file, canceled_output_file, num_passengers, passenger_weights, overweight_passengers, excessive_items_passengers)
