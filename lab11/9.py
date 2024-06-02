def main():
    with open('PASSENGERS.IN', 'r') as file:
        lines = file.readlines()
        num_passengers = int(lines[0].strip())
        passenger_weights = [list(map(float, line.strip().split())) for line in lines[1:]]
    total_weights = [sum(weights) for weights in passenger_weights]
    with open('WEIGHT.OUT', 'w') as weight_out_file:
        for weight in total_weights:
            weight_out_file.write(f'{weight:.2f}\n')
    canceled_passengers = []
    for i in range(num_passengers):
        if total_weights[i] > 23 or len(passenger_weights[i]) > 5:
            canceled_passengers.append(str(i + 1))
    with open('CANCELED.OUT', 'w') as canceled_out_file:
        canceled_out_file.write(' '.join(canceled_passengers))
    if canceled_passengers:
        print('Các hành khách sau đây đã bị hủy chuyến do vượt quá trọng lượng hoặc số lượng đồ xách tay:')
        print(' '.join(canceled_passengers))
    else:
        print('Không có hành khách nào bị hủy chuyến.')
if __name__ == '__main__':
    main()