# Đọc file PASSENGERS.IN
with open('PASSENGERS.IN', 'r') as file:
    lines = file.readlines()

# Lấy số lượng khách hàng
    num_passengers = int(lines[0].strip())
    weights = [list(map(float, line.split())) for line in lines[1:]]

# Tạo file WEIGHT.OUT và CANCELED.OUT
with open('WEIGHT.OUT', 'w') as weight_file, open('CANCELED.OUT', 'w') as canceled_file:
    for i, weight_list in enumerate(weights):
        total_weight = sum(weight_list)
# Ghi tổng trọng lượng vào WEIGHT.OUT
        weight_file.write(f'{total_weight}\n')

# Kiểm tra điều kiện hủy chuyến và ghi vào CANCELED.OUT
if total_weight > 23 or len(weight_list) > 5:
    canceled_file.write(f'{i+1}\n')  # i+1 vì số thứ tự bắt đầu từ 1

# In thông báo cụ thể về thông tin các hành khách bị hủy chuyến
with open('CANCELED.OUT', 'r') as file:
    canceled_passengers = file.readlines()

print("Thông tin hành khách bị hủy chuyến:")
for passenger in canceled_passengers:
    passenger_num = int(passenger.strip())
    weight_list = weights[passenger_num - 1]
    total_weight = sum(weight_list)
    num_items = len(weight_list)
    reason = "vượt quá 23 kg" if total_weight > 23 else "số lượng đồ xách tay vượt quá 5"
    print(f'Hành khách số {passenger_num} bị hủy chuyến do {reason}.')
