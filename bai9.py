input_file = 'lab11/package_9/PASSENGER.IN'
weight_output_file = 'lab11/package_9/WEIGHT.OUT'
canceled_output_file = 'lab11/package_9/CANCELED.OUT'

with open(input_file, 'r') as f:
    lines = f.readlines()

if len(lines) < 1:
    raise ValueError("File đầu vào trống hoặc thiếu dòng số lượng hành khách.")

num_passengers = int(lines[0].strip())

if len(lines) < num_passengers + 1:
    raise ValueError("File đầu vào không đủ dòng cho số lượng hành khách đã ghi.")

carry_on_weights = [list(map(float, line.split())) for line in lines[1:num_passengers + 1]]

total_weights = []
canceled_indices = []

for i, weights in enumerate(carry_on_weights, start=1):
    total_weight = sum(weights)
    num_items = len(weights)
    total_weights.append(total_weight)

    if total_weight > 23 or num_items > 5:
        canceled_indices.append(i)

with open(weight_output_file, 'w') as f:
    for weight in total_weights:
        f.write(f'{weight:.2f}\n')

with open(canceled_output_file, 'w') as f:
    for index in canceled_indices:
        f.write(f'{index}\n')

print("Thông tin hành khách bị hủy:")
for index in canceled_indices:
    passenger_weights = carry_on_weights[index - 1]
    total_weight = sum(passenger_weights)
    num_items = len(passenger_weights)

    if total_weight > 23:
        print(f"Hành khách {index} bị hủy: tổng trọng lượng {total_weight:.2f} kg vượt quá 23 kg.")
    if num_items > 5:
        print(f"Hành khách {index} bị hủy: số lượng hành lý {num_items} vượt quá 5.")