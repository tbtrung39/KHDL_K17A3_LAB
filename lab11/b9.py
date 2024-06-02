example_data = {
    "PASSENGERS.IN": "5\n20.5\n1.3 1.5 3.5 2 3\n7.25 3.5 7\n11 7 4.5 10 8.5 6\n4 6 8",
    "WEIGHT.OUT": "20.50\n11.50\n12.00\n35.00\n13.00",
    "CANCELD.OUT": "4\n5"
}
for filename, content in example_data.items():
    with open(filename, 'w') as file:
        file.write(content)
with open("PASSENGERS.IN", 'r') as file:
    num_passengers = int(file.readline().strip())
    weights = [float(file.readline().strip()) for _ in range(num_passengers)]
    canceled = [int(x) for x in file.readline().strip().split()]
with open("WEIGHT.OUT", 'w') as file:
    for weight in weights:
        file.write(f"{weight:2f}\n")
with open("CANCELED.OUT", 'w') as file:
    for idx in canceled:
        file.write(f"{idx:2f}\n")
    print("thong tin ca nhan hanh khach bi huy chuyen: ")
    for idx in canceled:
        print(f"so thu tu:{idx}")
        print(f"so luong do xach tay: {weights[idx-1]:.2f}kg")
        print()